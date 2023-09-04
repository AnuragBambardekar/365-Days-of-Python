list = [
    'Gems',
    'Munch',
    'Perk',
    'Kit-kat'
]

idx = list.index('Gems')
item = list.pop(idx)
list.append(item)
print(list)