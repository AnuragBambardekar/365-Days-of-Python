from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    # lon: float = 0.0
    # lat: float = 0.0
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))
    
oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
print( oslo.distance_to(vancouver))

# print(fields(Position))
lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)
