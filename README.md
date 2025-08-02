# Tesla FSD Trip Visualizer

Visualizes Tesla Full Self-Driving trip data from Washington DC to New York City on an interactive map.

## Features

- **Thick blue lines** showing FSD route segments
- **Big red dots** marking start and stop points
- **Duration labels** for segments longer than 3 miles
- **Non-overlapping labels** with alternating positions

## Setup

1. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

2. Run the visualizer:
   ```bash
   python simple_trip_visualizer.py
   ```

## Output

Generates `trip_map.html` - an interactive map showing your complete Tesla FSD journey with:
- Route visualization with thick blue lines
- Start/stop markers as red dots
- Duration labels for longer segments

## Data Format

The CSV file should contain tab-separated values with columns:
- `start_time` - Start time (e.g., "7:36 AM")
- `start_lat` - Start latitude
- `start_long` - Start longitude  
- `stop_time` - Stop time (e.g., "7:41 AM")
- `stop_lat` - Stop latitude
- `stop_long` - Stop longitude