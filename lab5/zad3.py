
liczba = input("Podaj liczbe: ")

odwrocona_liczba = ""
for cyfra in liczba:
    odwrocona_liczba = cyfra + odwrocona_liczba


if liczba == odwrocona_liczba:
    print(f"Liczba {liczba} jest palindromem.")
else:
    print(f"Liczba {liczba} nie jest palindromem.")

print(f"Odwrocona liczba: {odwrocona_liczba}")
