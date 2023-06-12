import ipaddress

# Create a list of IP networks
networks = [
    ipaddress.ip_network('192.168.1.0/24'),
    ipaddress.ip_network('192.168.2.0/24'),
    ipaddress.ip_network('192.168.3.0/24'),
    ipaddress.ip_network('192.168.4.0/24')
]

# Perform supernetting
supernet = ipaddress.ip_network(networks[0])
for network in networks[1:]:
    supernet = supernet.supernet(new_prefix=supernet.prefixlen-1)

# Print the resulting supernet
print("Supernet: ", supernet)
