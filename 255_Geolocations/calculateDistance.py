"""
Calculating distance between two coordinates
"""

from geopy.distance import great_circle

# Coordinates of two points
point1 = (52.2296756, 21.0122287)
point2 = (48.8588443, 2.2943506)

# Calculate distance using the Great Circle formula
distance = great_circle(point1, point2).kilometers

print(f"Distance: {distance} kilometers")
