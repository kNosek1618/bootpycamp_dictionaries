
from random import choice

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])


bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

item = False

for keys,value in bakery_stock.items():
    if food == keys:
        item = True
        print(f"{value} left")

if item == False:
    print("We don't make that")








