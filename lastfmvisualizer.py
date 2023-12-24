import requests 
import operator
import country_list

api_key = "4ce12ea4aaad9075ba836756e5d797ab"
base_api_url = "https://ws.audioscrobbler.com/2.0/"

api_token_call = f"https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key={api_key}&format=json"
token_call = requests.get(api_token_call)
method = "geo.getTopArtists"
token = token_call.json()['token']



def top_artists_from_regions():
    artists_listeners = {}
    country = "Iceland"
    method = "geo.getTopArtists"
    url = f"{base_api_url}?method={method}&country={country}&api_key={api_key}&limit=1000&format=json"
    getsession_call = requests.get(url)
    top_artists = getsession_call.json()
    
    
    #print(top_artists.values())
    
    for values in top_artists['topartists']['artist']:
        artists_listeners[values['name']] = values['listeners']
        
    artists_listeners = dict(sorted(artists_listeners.items(), key=operator.itemgetter(1)))

    
    for values2 in artists_listeners:
        print(f"{values2}: {artists_listeners[values2]}")
    
    
    return artists_listeners



        
        
    
    
top_artists_from_regions()


    





