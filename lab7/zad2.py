import random

krotka = tuple(random.randint(0, 10) for i in range(100))

print("Krotka 100-elementowa z losowymi liczbami od 0 do 10:")
print(krotka)

print(f"Liczba wsyatpien liczby 0: {krotka.count(0)}")
print(f"Liczba wsyatpien liczby 1: {krotka.count(1)}")
print(f"Liczba wsyatpien liczby 2: {krotka.count(2)}")

print("El parzyste: ")
for el in krotka:
    if el % 2 == 0:
        print(el)

print("El nie parzyste: ")
for el in krotka:
    if el % 2 != 0:
        print(el)   

dodatkowe_el = (1,2,4)
nowa_krotka = krotka + dodatkowe_el

print(nowa_krotka)