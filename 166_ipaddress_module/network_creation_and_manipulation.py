import ipaddress

# Creating a network
network = ipaddress.ip_network('192.168.0.0/24')

# Accessing network attributes
print(f"Network address: {network.network_address}")
print(f"Broadcast address: {network.broadcast_address}")
print(f"Number of hosts: {network.num_addresses}")

# Checking if an IP address is within the network
ip = ipaddress.ip_address('192.168.0.10')
if ip in network:
    print(f"{ip} is within the network")

# Iterating over hosts within the network
for host in network.hosts():
    print(host)
