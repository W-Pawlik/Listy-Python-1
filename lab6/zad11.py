# Wczytywanie wartości n
n = int(input("Podaj górną granicę zakresu (n): "))

if n < 2:
    print("Brak liczb pierwszych w podanym zakresie.")
else:
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if sito[i]:
            for j in range(i * i, n + 1, i):
                sito[j] = False

    liczby_pierwsze = [i for i, is_prime in enumerate(sito) if is_prime]

    print(f"Liczby pierwsze od 0 do {n}: {liczby_pierwsze}")
