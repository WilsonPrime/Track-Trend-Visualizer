import folium 
import requests
from folium.plugins import FastMarkerCluster

m = folium.Map(tiles="cartodbpositron")

geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
).json()

folium.GeoJson(geojson_data, name="hello world").add_to(m)

#folium.LayerControl().add_to(m)

for countries in range(len(geojson_data['features'])):
    print(geojson_data['features'][countries]['properties']['name'])
    #print(geojson_data['features'][countries]['geometry']['coordinates'])
    for coordinates in geojson_data['features'][countries]['geometry']['coordinates']:
        if(type(coordinates[0][0]) == list):
            folium.plugins.FastMarkerCluster(coordinates[0]).add_to(m)
        else:
            print(coordinates)
            folium.plugins.FastMarkerCluster(coordinates).add_to(m)
        #print()#folium.GeoJson(coordinates, name="bro", tooltip=geojson_data['features'][countries]['properties']['name']).add_to(m)
        #folium.PolyLine(locations=coordinates,popup=geojson_data['features'][countries]['properties']['name'])
        #folium.Marker(location=coordinates,popup=geojson_data['features'][countries]['properties']['name'])

    









m.save("index.html")