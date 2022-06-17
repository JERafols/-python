flavors = ["boots", "chocolate", "starwberry", "cookies n' cream", "bubble gum"]

toppings = ["almonds", "banana slice", "chocolate syrup", "caramel syrup", "white chocolate chips"]

ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachio", "ube": "mango slice"})
print(ice_cream)
