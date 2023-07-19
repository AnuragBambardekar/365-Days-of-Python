from collections import defaultdict

mylist = [1,2,3,2,1,3,4,5,1,2]
print(mylist)
counter = defaultdict(int)

for element in mylist:
    counter[str(element)] += 1

print(counter)
