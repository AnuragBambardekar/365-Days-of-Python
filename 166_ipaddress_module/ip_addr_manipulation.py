import ipaddress

# Creating IP addresses
ip1 = ipaddress.ip_address('192.168.0.1')
ip2 = ipaddress.ip_address('192.168.0.2')

# Comparing IP addresses
if ip1 < ip2:
    print(f"{ip1} is less than {ip2}")
elif ip1 > ip2:
    print(f"{ip1} is greater than {ip2}")
else:
    print(f"{ip1} is equal to {ip2}")

# Converting IP address to integer and back
ip_int = int(ip1)
ip_from_int = ipaddress.ip_address(ip_int)
print(f"Integer representation: {ip_int}")
print(f"IP address from integer: {ip_from_int}")

