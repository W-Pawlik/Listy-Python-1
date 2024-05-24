krotka = ("pierwszy", 2,3,"cztery",5,10)

print(krotka)
print(len(krotka))
print(id(krotka))

krotka+=("cos",2)

print(krotka)
print(id(krotka))

lista = list(krotka)
print(lista)