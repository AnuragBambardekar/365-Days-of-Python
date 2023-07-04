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


from collections import ChainMap

english = {"apple": "Apple", "banana": "Banana", "orange": "Orange"}
french = {"apple": "Pomme", "banana": "Banane", "orange": "Orange"}
spanish = {"apple": "Manzana", "banana": "Plátano", "orange": "Naranja"}

translations = {
    "en": ChainMap(english),
    "fr": ChainMap(french),
    "es": ChainMap(spanish)
}

print(translations["en"]["apple"])  # Output: Apple
print(translations["fr"]["apple"])  # Output: Pomme
print(translations["es"]["apple"])  # Output: Manzana