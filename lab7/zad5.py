
krotka1 = ('pociag',)
krotka2 = ('tramwaj',)

# Pobranie słów z krotek
slowo1 = krotka1[0]
slowo2 = krotka2[0]

# Sprawdzenie, czy słowa są anagramami
if sorted(slowo1) == sorted(slowo2):
    print(f"Slowa '{slowo1}' i '{slowo2}' sa anagramami.")
else:
    print(f"Slowa '{slowo1}' i '{slowo2}' nie sa anagramami.")


print("Przykladowe anagramy: bark- krab ")
krotka3 = ('bark',)
krotka4 = ('krab',)

slowo3 = krotka3[0]
slowo4 = krotka4[0]

if sorted(slowo3) == sorted(slowo4):
    print(f"Slowa '{slowo3}' i '{slowo4}' sa anagramami.")
else:
    print(f"Slowa '{slowo3}' i '{slowo4}' nie sa anagramami.")