x = int(input("Wprowadz x: "))
z = int(input("Wprowadz z: "))
tab = []

for i in range(x, z+1):
    tab.append(i)
    print(i)

print(f'Trzeci element od konca to: {tab[-3]}')

k = int(input("Wprowadz ktory indeks elementu od konca chcesz usunac: "))
tab.pop(-k)
print(tab)

x2 = int(input("Wprowadz x2: "))
z2 = int(input("Wprowadz z2: "))
tab2 = []

for i in range(x2, z2+1):
    tab.append(i)
    tab2.append(i)
    print(i)

print(f'Scalona lista: {tab}')
print(f'Dlugosc listy: {len(tab)}')


ilosc_wystapienia = {}
for liczba in tab:
    ilosc_wystapienia[liczba] = tab.count(liczba)

print("Wystąpienia każdej liczby:")
for liczba, ilosc in ilosc_wystapienia.items():
    print(f"Liczba {liczba}: {ilosc} razy")

