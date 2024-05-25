# Inicjalizacja zmiennych
poprzednia_liczba = None
licznik = 0

while True:
    liczba = int(input("Podaj liczbe: "))
    licznik += 1
    
    if poprzednia_liczba != None:
        roznica = abs(liczba - poprzednia_liczba)
        if roznica < 5:
            print("Wartosc bezwzględna roznicy między dwoma kolejnymi liczbami jest mniejsza od 5.")
            break
    
    poprzednia_liczba = liczba

print("Ilosc wprowadzonych liczb:", licznik)
