
n = int(input("Podaj liczbe elementow: "))

liczby = []
for i in range(n):
    liczba = int(input(f"Podaj liczbę {i+1}: "))
    liczby.append(liczba)

najwieksza_liczba = max(liczby)
liczba_wystapien = liczby.count(najwieksza_liczba)

print(f"Największa liczba: {najwieksza_liczba}")
print(f"Największa liczba wystąpiła {liczba_wystapien} razy")
