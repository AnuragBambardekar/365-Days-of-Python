import pandas as pd

df = pd.read_excel('270_One_Byte_that_destroys/data.xlsx')
# print(df) 
print(df.email.values[2]) 
print(df.email.values[2] == "bob@gmail.com")
# print(df.email.values[2].encode('ascii')) # cannot do it

# "​" - zero width byte
"""
how to type in windows:
hold alt
type +
type 200B
release alt
"""

print(df.email.values[2].encode('utf-8'))

# Let's try to construct it
mystring = "Hello W\u200dorld"
# print(mystring.encode('ascii'))

# Fixing it by filtering out the zero width bytes
mystring = mystring.replace('\u200d','')
mystring = mystring.replace('\u200c','')
mystring = mystring.replace('\u200b','')
print(mystring.encode('ascii'))
