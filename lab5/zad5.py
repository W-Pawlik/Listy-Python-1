
suma_szescianow = 0
for i in range(101):
    suma_szescianow += i ** 3

print(f"Suma szescianow liczb naturalnych od 0 do 100 wynosi: {suma_szescianow}")

suma_szescianow = 0
i = 0
while suma_szescianow <= 10**6:
    suma_szescianow += i ** 3
    i += 1

print(f"Aby suma sześcianow liczb naturalnych byla wieksza niz 10^6, trzeba zsumowac {i} liczb.")
