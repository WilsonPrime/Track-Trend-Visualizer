import pydeck
import requests

geojson_data = requests.get(
    "https://raw.githubusercontent.com/WilsonPrime/Visualizer/master/new2.json"
).json()

DATA_URL = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
LAND_COVER = [[[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]]



print()

INITIAL_VIEW_STATE = pydeck.ViewState(
  latitude=49.254,
  longitude=-123.13,
  zoom=11,
  max_zoom=16,
  pitch=45,
  bearing=0
)

polygon = pydeck.Layer(
    'PolygonLayer',
    LAND_COVER,
    stroked=False,
    # processes the data as a flat longitude-latitude pair
    get_polygon='-',
    get_fill_color=[0, 0, 0, 20]
)


geojson = pydeck.Layer(
            'GeoJsonLayer',
            geojson_data,
            #get_elevation= 50,
            get_elevation=500,
            get_fill_color=[255,0,0,150],
            get_line_color=[40, 100, 50],
            elevation_scale = 50,
            pickable=True
        )
    

r = pydeck.Deck(
    layers=[geojson],
    initial_view_state=INITIAL_VIEW_STATE)

r.to_html("hello.html")