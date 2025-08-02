import pandas as pd
import folium
import os
from datetime import datetime
from geopy.distance import geodesic

def calculate_duration(start_time, stop_time):
    try:
        start = datetime.strptime(start_time, '%I:%M %p')
        stop = datetime.strptime(stop_time, '%I:%M %p')
        if stop < start:
            stop = stop.replace(day=start.day + 1)
        duration = stop - start
        return int(duration.total_seconds() / 60)
    except:
        return 0

def create_trip_map():
    # Load data
    df = pd.read_csv('data/fsd-start-stop.csv', sep='\t')
    
    # Calculate center
    all_lats = list(df['start_lat']) + list(df['stop_lat'])
    all_longs = list(df['start_long']) + list(df['stop_long'])
    center_lat = sum(all_lats) / len(all_lats)
    center_long = sum(all_longs) / len(all_longs)
    
    # Create map
    m = folium.Map(location=[center_lat, center_long], zoom_start=8)
    
    for idx, row in df.iterrows():
        start_coords = [row['start_lat'], row['start_long']]
        stop_coords = [row['stop_lat'], row['stop_long']]
        
        # Thick blue line
        folium.PolyLine(
            locations=[start_coords, stop_coords],
            color='blue',
            weight=6,
            opacity=0.8
        ).add_to(m)
        
        # Big red dots for start/stop
        folium.CircleMarker(
            location=start_coords,
            radius=8,
            color='red',
            fill=True,
            fillColor='red'
        ).add_to(m)
        
        folium.CircleMarker(
            location=stop_coords,
            radius=8,
            color='red',
            fill=True,
            fillColor='red'
        ).add_to(m)
        
        # Labels for segments > 5 miles
        distance_miles = geodesic(start_coords, stop_coords).miles
        if distance_miles > 3:
            duration_mins = calculate_duration(row['start_time'], row['stop_time'])
            # Alternate label positions to avoid overlap
            lat_offset = 0.03 if idx % 2 == 0 else -0.03
            lng_offset = 0.08 + (idx % 3) * 0.02
            mid_lat = (start_coords[0] + stop_coords[0]) / 2 + lat_offset
            mid_lng = (start_coords[1] + stop_coords[1]) / 2 + lng_offset
            
            folium.Marker(
                location=[mid_lat, mid_lng],
                icon=folium.DivIcon(html=f'<div style="background:white;color:black;padding:8px 10px;border:1px solid black;border-radius:5px;font-size:20px;font-weight:bold;min-width:120px;text-align:center;">{duration_mins}min</div>')
            ).add_to(m)
    
    m.save('trip_map.html')
    print("Map saved as trip_map.html")

if __name__ == "__main__":
    create_trip_map()