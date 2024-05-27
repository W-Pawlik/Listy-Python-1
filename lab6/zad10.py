n = int(input("Podaj liczbę elementów ciągu Fibonacciego: "))

fib = []
if n >= 1:
    fib.append(0)  
if n >= 2:
    fib.append(1)  

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(f"Początkowe {n} liczb Fibonacciego: {fib}")
