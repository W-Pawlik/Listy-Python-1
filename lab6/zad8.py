import random

liczby = random.sample(range(1, 100), 6)
print("Wylosowane liczby:", liczby)

random.shuffle(liczby)
print("Po wymieszaniu:", liczby)

liczby.sort()
print("Po posortowaniu:", liczby)
