
n = int(input("Podaj ilosc liczb: "))

for i in range(n):
    liczba = int(input(f"Podaj liczbe {i+1}: "))
    if -6 <= liczba <= 6:
        print(f"Liczba {liczba} jest z przedzialu [-6, 6].")
    else:
        print(f"Liczba {liczba} nie jest z przedzialu [-6, 6].")
