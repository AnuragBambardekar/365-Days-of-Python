import hashlib

h = hashlib.new("SHA256")
correct_pass = "passWord9090"
h.update(correct_pass.encode())

pass_hash = h.hexdigest()
print(pass_hash)

user_input = "passWord9090"
h = hashlib.new("SHA256")
h.update(user_input.encode())
input_hash = h.hexdigest()
print(input_hash)

print(input_hash == pass_hash)