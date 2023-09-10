"""
how to get Geolocation when you enter any location name

pip install geopy
"""

from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode("New Brunswick New Jersey")

print(getLoc.address)
print("Latitude: ", getLoc.latitude)
print("Longitude: ", getLoc.longitude)


"""
from geopy.geocoders import Nominatim

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Perform geocoding
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")

"""