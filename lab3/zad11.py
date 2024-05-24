import random

wylosowane = []

while len(wylosowane) < 5:
    liczba = random.randint(1, 42)
    if liczba not in wylosowane:
        wylosowane.append(liczba)


# Wyświetlenie wylosowanych liczb
print("Wylosowane liczby to:", wylosowane)

trafione = 0
for _ in range(6):
    strzal = int(input(f'Strzel {_+1} liczbe: '))
    if strzal in wylosowane:
        trafione += 1
    
print("Liczba trafioncy liczb: ", trafione)