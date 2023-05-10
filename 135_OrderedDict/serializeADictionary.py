import json
from collections import OrderedDict

# Create a dictionary with some keys in a specific order
data = OrderedDict()
data['name'] = 'John'
data['age'] = 30
data['city'] = 'New York'

# Serialize the dictionary in order using json.dumps()
serialized_data = json.dumps(data)

# Print the serialized data
print(serialized_data)
