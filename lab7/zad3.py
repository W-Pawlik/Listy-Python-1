import random

krotka_A = tuple(random.randint(0, 50) * 2 for _ in range(100))

krotka_B = tuple(random.randint(0, 50) * 2 + 1 for _ in range(100))


krotka_C = krotka_A + krotka_B

print("Długość krotki po konkatenacji:", len(krotka_C))

# Sprawdzenie czy krotka zawiera liczby 0 i 100
czy_zawiera_0 = 0 in krotka_C
czy_zawiera_100 = 100 in krotka_C
print("Czy krotka zawiera liczbę 0?", czy_zawiera_0)
print("Czy krotka zawiera liczbę 100?", czy_zawiera_100)

