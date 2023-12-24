import requests 
import operator
import country_list
import json
import pycountry

api_key = "4ce12ea4aaad9075ba836756e5d797ab"
base_api_url = "https://ws.audioscrobbler.com/2.0/"

api_token_call = f"https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key={api_key}&format=json"
token_call = requests.get(api_token_call)
method = "geo.getTopArtists"
token = token_call.json()['token']



def top_artists_from_regions(country_name):
    artists_listeners = {}
    country_top_1000 = {}
    #country_name = "United States"
    method = "geo.getTopArtists"
    url = f"{base_api_url}?method={method}&country={country_name}&api_key={api_key}&limit=1000&format=json"
    getsession_call = requests.get(url)
    top_artists = getsession_call.json()
    
    
    #print(top_artists.values())
    try:
        for values in top_artists['topartists']['artist']:
            artists_listeners[values['name']] = values['listeners']
            artists_listeners = dict(sorted(artists_listeners.items(), key=operator.itemgetter(1)))
    except KeyError:
        pass
    
    #for values2 in artists_listeners:
        #print(f"{values2}: {artists_listeners[values2]}")
    
    country_top_1000[f"{country_name}"] = artists_listeners
    
    return country_top_1000


request_table = requests.get("https://raw.githubusercontent.com/WilsonPrime/Visualizer/master/data.json")
coordinate_table = json.loads(request_table.text)
#print(coordinate_table.keys())


#print(coordinate_table['features'][0])
#coordinate_table.update()
#print(json.dumps(coordinate_table))


country_artists = []
#country_artists.append(top_artists_from_regions())
for country in pycountry.countries:
 #   print(country.name)
    country_artists.append(top_artists_from_regions(country.name))

#print(country_artists[0].values())

for countries in country_artists:
    #print(countries)
    current_country = list(countries.keys())[0]
#print(coordinate_table['features'][0]['properties'])
    try:
        for object in coordinate_table['features']:
            if(object['properties']['name'] == current_country):
                print("Did it break here?")
                object['properties']['artists'] = countries[current_country]
            else:
                pass
    except KeyError:
        print("didnt exist")


#for object in coordinate_table:
 #   if(object['properties']['name'] == current_country)

#for values in range(len(coordinate_table['features'])):
 #   current_country = coordinate_table['features'][values]['properties']['name']
  #  coordinate_table[current_country] = country_artists[cur].values()


updated_json_string = json.dumps(coordinate_table, indent=2)

with open("new.sjon", "w") as file:
    file.write(updated_json_string)




