import requests

def get_geocoordinates_from_address(address: str) -> tuple:
    url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={address}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    
    response = requests.get(url)    
    data = response.json()

    # Check if there are results
    if data['results']:
        first_result = data['results'][0]
        latitude = first_result['LATITUDE']
        longitude = first_result['LONGITUDE']
        return (latitude, longitude)
    else:
        return ("NA", "NA")