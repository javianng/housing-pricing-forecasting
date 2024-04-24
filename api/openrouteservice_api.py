import os
import requests

from dotenv import load_dotenv


load_dotenv()
API_KEY_2 = os.getenv("OPEN_ROUTE_SERVICE_API_KEY")


class Coordinate:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def get_lon(self):
        return self.lon
    
    def get_lat(self):
        return self.lat


def get_distance_between_two_coordinates(start: Coordinate, end: Coordinate) -> float:
    # Create the URL for the Directions API
    url = 'https://api.openrouteservice.org/v2/directions/driving-car'

    params = {
        'api_key': API_KEY_2,
        'start': f"{start.get_lon()},{start.get_lat()}",
        'end': f"{end.get_lon()},{end.get_lat()}"
    }

    # Make the request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the distance from the response (in meters)
        distance = data['features'][0]['properties']['segments'][0]['distance']

        # convert distance to kilometers
        distance = distance / 1000
    else:
        distance = None
    return distance