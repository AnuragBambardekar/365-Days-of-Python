import dis

def hello_world():
    msg = "Hello World!"
    return msg

print(dis.dis(hello_world)) # returns the python bytecode