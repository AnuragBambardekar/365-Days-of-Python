from geopy.geocoders import Nominatim
import json

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Perform geocoding
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

# Convert the location data to GeoJSON format
geojson_data = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [location.longitude, location.latitude]
    },
    "properties": {
        "address": location.address
    }
}

# Serialize the GeoJSON data to a JSON string
geojson_string = json.dumps(geojson_data, indent=2)
print(geojson_string)
