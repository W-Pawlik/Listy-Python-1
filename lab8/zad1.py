
menu = {
    "Pizza Margherita": 25.00,
    "Pizza Pepperoni": 28.50,
    "Burger Classic": 22.00,
    "Sałatka Cezar": 18.50,
    "Spaghetti Bolognese": 26.00,
    "Zupa Pomidorowa": 15.00,
    "Lasagna": 30.00,
    "Sushi": 35.00,
    "Stek wołowy": 50.00,
    "Tiramisu": 20.00
}

print("Wartości (ceny):")
for value in menu.values():
    print(value)

print("\nKlucze (nazwy dan):")
for key in menu.keys():
    print(key)

print("\nKlucze i wartosci (menu):")
for key, value in menu.items():
    print(f"{key}: {value} zl")

lowest_price_item = min(menu, key=menu.get)
highest_price_item = max(menu, key=menu.get)
del menu[lowest_price_item]
del menu[highest_price_item]

print("\nMenu po usunieciu elementu o najnizszej i najwyzszej cenie:")
for key, value in menu.items():
    print(f"{key}: {value} zl")

menu["Pizza Hawajska"] = 19.99

print("\nMenu po dodaniu nowej pozycji:")
for key, value in menu.items():
    print(f"{key}: {value} zl")
