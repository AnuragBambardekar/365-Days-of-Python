import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

"""
hashlib.algorithms_guaranteed lists only the hashing algorithms that you 
can safely assume will be available on any system where Python is 
installed, while hashlib.algorithms_available lists all available 
algorithms, including those that might not be present on all systems.
"""

h = hashlib.new("SHA256")
h.update(b"Hello World!")

# returns the hash as bytes. In the case of SHA-256, the digest will 
# be a 32-byte (256-bit) binary string.
print(h.digest())

# converts the binary hash value into a hexadecimal string, making it 
# more human-readable.
print(h.hexdigest())
