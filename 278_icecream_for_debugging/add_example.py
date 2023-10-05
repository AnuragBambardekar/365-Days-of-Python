from icecream import ic

# def myfunc(a,b,c):
#     for _ in range(10):
#         print(a,b,a==b)
#         print(type(a),type(b))
#         if a==b:
#             pass
#         else:
#             if c%2 == 0:
#                 pass
#             else:
#                 pass

def add(x,y):
    return x+y

# print(add(10,20))
# print(add(40,20))
# print(add(30,20))
# print(add(10,50))
# print(add(10,90))

res = ic(add(10,20))
print(res)

ic(add(10,20))
ic(add(40,20))
ic(add(30,20))
ic(add(10,50))
ic(add(10,90))