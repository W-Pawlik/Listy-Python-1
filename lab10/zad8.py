import random

def sum_of_squares(n):
    return (n * (n + 1) * (2*n + 1)) // 6

def main():
    n = random.randint(0, 1000)
    result = sum_of_squares(n)
    print(f"Losowo wybrana liczba n: {n}")
    print(f"Suma kwadratow liczb od 0 do {n} wynosi: {result}")

if __name__ == "__main__":
    main()
