from collections import ChainMap

# define dictionaries for English, French, and Spanish translations
en_dict = {'apple': 'apple', 'orange': 'orange', 'banana': 'banana'}
fr_dict = {'apple': 'pomme', 'orange': 'orange', 'banana': 'banane'}
es_dict = {'apple': 'manzana', 'orange': 'naranja', 'banana': 'plátano'}

# create a ChainMap with the three translation dictionaries
translations = ChainMap(en_dict, fr_dict, es_dict)

# lookup translations
print(translations['apple'])  # output: 'apple' (from en_dict)
print(translations['orange']) # output: 'orange' (from fr_dict)
print(translations['banana']) # output: 'banana' (from en_dict)

# modify translations
translations['apple'] = 'pomme'
translations['banana'] = 'banane'

# verify that the original dictionaries are unchanged
print(en_dict)
print(fr_dict) 
print(es_dict) 
