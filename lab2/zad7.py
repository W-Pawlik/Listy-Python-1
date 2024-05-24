
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("Rozwiązania równania kwadratowego:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Rozwiązanie równania kwadratowego:")
    print("x =", x)
else:
    print("Brak rozwiązań rzeczywistych dla podanych współczynników.")
