from geopy.geocoders import Nominatim

geoLoc = Nominatim(user_agent="GetLoc")

locname = geoLoc.reverse("40.4862174, -74.4518173")

print(locname.address)

"""
from geopy.geocoders import Nominatim

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Perform reverse geocoding
location = geolocator.reverse("37.4219999,-122.0840575")

print(location.address)

"""