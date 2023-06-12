import ipaddress

# Defining an IP address
ip = '10.10.10.0/28'

# Creating an ip_network object
net1 = ipaddress.ip_network(ip)

"""
A subnet, short for subnetwork, is a logical subdivision of an IP network. It is created by dividing a larger network into smaller, more manageable segments. 
Subnetting allows for efficient allocation of IP addresses and helps with network management and security.
"""

"""
A subnet allows for further partitioning of the IP address space, enabling devices within the same subnet to communicate directly with each other without 
the need for routing through other subnets.
"""


print("Subnet: ", net1.network_address)
print("Broadcast Address: ", net1.broadcast_address)
print("WildCard Mask: ", net1.hostmask)
print("Subnet Mask: ", net1.netmask)
print("Network / Mask: ", net1.with_netmask)
print("CIDR Format: ", net1.with_prefixlen)
print("CIDR Length: ", net1.prefixlen)
print("Total Addresses: ", net1.num_addresses)

for host in net1.hosts():
    print(host)

# let's divide /28 into multiple of /30
for host in net1.subnets(new_prefix= 30):
    print(host)