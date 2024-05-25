import random

wylosowana_liczba = random.randint(1, 100)
proby = 3

for i in range(proby):
    strzal = int(input(f"Proba {i+1}: Podaj liczbe: "))
    
    if strzal > wylosowana_liczba:
        print("Podales za dużą wartosc.")
    elif strzal < wylosowana_liczba:
        print("Podales za mala wartosc.")
    else:
        print("Gratulacje! Odgadles liczbe.")
        break
else:
    print("Haha przegrales")
    print(f"Wylosowana liczba to: {wylosowana_liczba}")

