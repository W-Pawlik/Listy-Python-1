# Pobieranie liczby od użytkownika
liczba = input("Podaj liczbę: ")

# Sprawdzanie, czy podana wartość jest liczbą całkowitą
if liczba.isdigit():
    liczba = int(liczba)
    
    if liczba < 1:
        print("Liczba musi być większa niż 0.")
    else:
        # Obliczanie sumy dzielników właściwych
        suma_dzielnikow = 0
        for i in range(1, liczba):
            if liczba % i == 0:
                suma_dzielnikow += i
        
        # Sprawdzanie, czy liczba jest doskonała
        if suma_dzielnikow == liczba:
            print("Liczba jest doskonala")
        else:
            print("Liczba nie jest doskonala")
else:
    print("To nie jest liczba.")
