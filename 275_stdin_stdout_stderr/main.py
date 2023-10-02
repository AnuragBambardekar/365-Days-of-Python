import sys

print("Hello World!", end=" ")
print("Hello World!")
sys.stdout.write("Hello World!\n")

sys.stderr.write("This is an error")

print(input())
print(sys.stdin.read()) # multiple lines of input - infinite



