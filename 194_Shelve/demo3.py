""" Using PICKLES
import json
class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
    
    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')

if __name__ == "__main__":
    fruit: Fruit = Fruit('Banana', 100)
    fruit.describe_fruit()

    fruit.calories = 150

    with open('banana.json', 'w') as file:
        # add data to json file
        data = {'name': fruit.name, 'calories':fruit.calories}
        json.dump(data, file)
"""


#=============Using Shelve==============#

import shelve

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories
    
    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')

data: dict = {
    'apple':Fruit('Apple',10),
    'banana':Fruit('Banana',10),
    'orange':Fruit('Orange',10),
}

with shelve.open('194_Shelve/FruitsDB') as db:
    # db.update(data)
    print(dict(db)) # Fruit objects
    apple = db['apple']

apple.describe_fruit()
print(apple)
