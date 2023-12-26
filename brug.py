import pydeck
import requests
import json

geojson_data = requests.get(
    "https://raw.githubusercontent.com/WilsonPrime/Visualizer/master/newtrack.json"
).json()

DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
LAND_COVER = [[[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]]




INITIAL_VIEW_STATE = pydeck.ViewState(
  latitude=49.254,
  longitude=-123.13,
  zoom=11,
  max_zoom=16,
  pitch=45,
  bearing=0
)

import json

# Read the original JSON data from the file
with open('newtrack.json', 'r') as file:
    geojson_data = json.load(file)

# Filter out entries without 'artists' property
filtered_features = [
    feature for feature in geojson_data['features'] if 'artists' in feature['properties']
]

# Update the JSON data with filtered features
geojson_data['features'] = filtered_features

# Write the updated JSON data back to the file
with open('newtrack.json', 'w') as file:
    json.dump(geojson_data, file, indent=2)

# Print information after filtering
# Print information after filtering
for i, feature in enumerate(geojson_data['features']):
    artists_key_present = 'artists' in feature['properties']
    print(f"Feature {i + 1}: 'artists' key present - {artists_key_present}")






# Create the GeoJSON layer with the extracted values
geojson = pydeck.Layer(
    'GeoJsonLayer',
    geojson_data,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation='properties.artists.TotalListeners / 1000',
    get_fill_color='[0, 50, 150, 150]',
    get_line_color=[40, 100, 50],
    elevation_scale=0.5,

    pickable=True
)

r = pydeck.Deck(
    layers=[geojson],
    initial_view_state=INITIAL_VIEW_STATE)

r.to_html("hello.html")