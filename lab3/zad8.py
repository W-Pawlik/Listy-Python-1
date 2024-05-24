
for liczba in range(999, 0, -1):
    if liczba % 2 != 0 and liczba % 3 != 0 and liczba % 5 != 0 and liczba % 7 != 0:
        najwieksza = liczba
        break

print("Największa liczba mniejsza od 1000, która nie jest podzielna przez 2, 3, 5 ani 7 to:", najwieksza)
