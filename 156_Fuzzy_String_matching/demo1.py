# pip install thefuzz

from thefuzz import fuzz, process

# s1 = "Hello World"
# s2 = "hello world"

# print(s1 is s2)
# print(s1 == s2)

s1 = "Just a Test"
s2 = "Just a Test and this is a long strinf"
s3 = "Something completely different"
s4 = "Just a Test and some more"

print(fuzz.ratio(s1,s2))
print(fuzz.ratio(s1,s3))
print(fuzz.partial_ratio(s1,s4))

s5 = "Hello World is the basic"
s6 = "The basic is Hello World"

print(fuzz.partial_ratio(s5,s6))
print(fuzz.ratio(s5,s6))
print(fuzz.token_sort_ratio(s5,s6))

print()

s7 = "Hello World"
s8 = "Hello Hello World World World"

print(fuzz.ratio(s7,s8))
print(fuzz.partial_ratio(s7,s8))
print(fuzz.token_sort_ratio(s7,s8))
print(fuzz.token_set_ratio(s7,s8))