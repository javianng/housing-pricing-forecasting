import requests

def get_bto_coordinates(bto):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": bto,
        "format": "json",
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json()
        if results:
            # Extract latitude and longitude from the first result
            lat = results[0]['lat']
            lon = results[0]['lon']
            return lat, lon
        else:
            return None, None
    else:
        # print("API request failed:", response.status_code)
        return None, None
    
# print(get_bto_coordinates("Kallang Whampoa King George’s Heights (PLH)")) # - (None, None) because not built yet
