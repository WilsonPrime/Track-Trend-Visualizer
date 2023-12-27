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
  pitch=200,
  bearing=0
)


with open('newtrack.json', 'r') as file:
    geojson_data = json.load(file)

filtered_features = [
    feature for feature in geojson_data['features'] if 'artists' in feature['properties']
]

geojson_data['features'] = filtered_features

with open('newtrack.json', 'w') as file:
    json.dump(geojson_data, file, indent=2)


total_listeners = []

for i, feature in enumerate(geojson_data['features']):
    artists_key_present = 'artists' in feature['properties']
    data = feature['properties']['artists']['TotalListeners']
    if(data != 1):
        total_listeners.append(data)
    print(f"Feature {i + 1}: 'artists' key present - {artists_key_present} and total {data}")


minimum = min(total_listeners)
maximum = max(total_listeners)


geojson = pydeck.Layer(
    'GeoJsonLayer',
    geojson_data,

    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
    get_elevation='properties.artists.TotalListeners',
    get_fill_color='[60 , 100, 150, 150]',
    get_line_color=[0, 100, 50],
    elevation_scale=0.001,
    elevation_range = [minimum,maximum],

    pickable=True
)

r = pydeck.Deck(
    layers=[geojson],
    initial_view_state=INITIAL_VIEW_STATE)

r.to_html("hello.html")