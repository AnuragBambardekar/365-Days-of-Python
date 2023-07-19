from collections import defaultdict

tuple_list = [("A",10), ("B",4), ("A",5), ("C",7), ("B",1)]
grouped_data = defaultdict(list)

for key, val in tuple_list:
    grouped_data[key].append(val) # list of values

print(grouped_data)

grouped_data = {k: sum(v) for k,v in grouped_data.items()}
print(grouped_data)