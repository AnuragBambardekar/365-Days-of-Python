import ipaddress

# Working with IPv6 addresses
ipv6 = ipaddress.ip_address('2001:0db8::1')
print(f"IP version: {ipv6.version}")
print(f"Compressed representation: {ipv6.compressed}")
print(f"Exploded representation: {ipv6.exploded}")

# Checking if an IPv6 address is within a network
network = ipaddress.ip_network('2001:0db8::/64')
if ipv6 in network:
    print(f"{ipv6} is within the network")

# Subnetting an IPv6 network
subnets = network.subnets(new_prefix=80)
for subnet in subnets:
    print(subnet)
