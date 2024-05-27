import random

wylosowane = []

while len(wylosowane) < 6:
    liczba = random.randint(1, 49)
    if liczba not in wylosowane:
        wylosowane.append(liczba)


# Wyświetlenie wylosowanych liczb
print("Wylosowane liczby to:", wylosowane)

losy = []
trafione = 0

for i in range(6):
    los = int(input("Wprowadz los: "))
    losy.append(los)
    if los in wylosowane:
        trafione += 1
print(losy)

print("Liczba trafioncy liczb: ", trafione)

match trafione:
    case 6:
        print("Wygrana 1000000 zl!")
    case 5:
        print("Wygrana 5000 zl!")
    case 4:
        print("Wygrana 100 zl!")
    case 3:
        print("Wygrana 10 zl!")
    case _:
        print("Wygrana 0 zl!")




