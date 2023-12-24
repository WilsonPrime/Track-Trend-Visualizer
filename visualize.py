import requests 
import base64

def token_generation():
    client_id = "b8d689ceb7b2439a8b059e95247583a1"
    client_secret = "91ee8be24d4d4902a07e33cd18f3fe7c"
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
    token_url = "https://accounts.spotify.com/api/token"


    token_params = {
        "grant_type": "client_credentials"
    }

    token_headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }


    token_response = requests.post(token_url, data=token_params, headers=token_headers)
    token_data = token_response.json()


    access_token = token_data['access_token']
    token_type = token_data['token_type']
    time_to_expire = token_data['expires_in']


    return access_token, token_type, time_to_expire


def getAlbum(token):
    token_url = "https://api.spotify.com/v1/artists/2HPaUgqeutzr3jx5a9WyDV"

    token_headers = {
        "Authorization": f"Bearer {token}",
        "Accept": 'application/json'
    }

    data = requests.get(token_url,headers=token_headers)

    print(data.json())
    return data


def main():
    token, token_type, expiration_timer = token_generation()
    artist_info = getAlbum(token)



main()