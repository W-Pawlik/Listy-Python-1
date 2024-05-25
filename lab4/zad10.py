# Inicjalizacja zmiennych
poprzednia_liczba = None
suma = 0

while True:
    liczba = int(input("Podaj liczbe: "))
    suma += liczba
    
    if poprzednia_liczba is not None and liczba == poprzednia_liczba:
        print("Dwie kolejne liczby są takie same.")
        break
    
    poprzednia_liczba = liczba

print("Suma wprowadzonych liczb:", suma)
