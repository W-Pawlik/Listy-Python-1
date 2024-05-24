
liczba = int(input("Wprowadz liczbe wieksza od 1: "))
suma = 1

for i in range(2, liczba+1):
    if liczba > 1:
        suma *= i
        
print(suma)
