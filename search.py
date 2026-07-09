from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="GeoBoundaryFinder")

def search_location(place):

    location = geolocator.geocode(place)

    if location:

        return {

            "name": location.address,

            "lat": location.latitude,

            "lon": location.longitude

        }

    return None