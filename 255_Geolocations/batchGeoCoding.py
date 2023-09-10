from geopy.geocoders import Nominatim

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# List of addresses to geocode
addresses = ["1600 Amphitheatre Parkway, Mountain View, CA", "Eiffel Tower, Paris"]

for address in addresses:
    location = geolocator.geocode(address)
    if location:
        print(f"Address: {address}, Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print(f"Address not found for: {address}")
