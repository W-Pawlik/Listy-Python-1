# Pobieranie danych od użytkownika
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))
d = float(input("Podaj czwartą liczbę: "))

# Sprawdzenie wszystkich możliwych kombinacji
if a >= b and a >= c and a >= d:
    najwieksza = a
elif b >= a and b >= c and b >= d:
    najwieksza = b
elif c >= a and c >= b and c >= d:
    najwieksza = c
else:
    najwieksza = d

# Wyświetlenie największej liczby
print("Największa liczba to:", najwieksza)
