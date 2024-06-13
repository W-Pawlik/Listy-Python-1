
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
numer_telefonu = input("Podaj swój numer telefonu: ")
numer_buta = input("Podaj swój numer buta: ")

imie_isalpha = imie.isalpha()
nazwisko_isalpha = nazwisko.isalpha()

telefon_isdigit = numer_telefonu.isdigit()
but_isdigit = numer_buta.isdigit()

imie_corrected = imie.capitalize()
nazwisko_corrected = nazwisko.capitalize()

numer_telefonu_cleaned = ''.join(filter(str.isdigit, numer_telefonu))
numer_buta_cleaned = ''.join(filter(str.isdigit, numer_buta))

female_endings = ["a", "na", "ra", "la", "ela", "ika", "eta", "nia", "ina", "yna", "ewa", "ura", "zia"]
is_female = any(imie_corrected.endswith(ending) for ending in female_endings)

print(f"\nWyniki:")
print(f"Imię składa się tylko z liter: {imie_isalpha}")
print(f"Nazwisko składa się tylko z liter: {nazwisko_isalpha}")
print(f"Numer telefonu składa się wyłącznie z cyfr: {telefon_isdigit}")
print(f"Numer buta składa się wyłącznie z cyfr: {but_isdigit}")

print(f"Poprawione imię: {imie_corrected}")
print(f"Poprawione nazwisko: {nazwisko_corrected}")

print(f"Oczyszczony numer telefonu: {numer_telefonu_cleaned}")
print(f"Oczyszczony numer buta: {numer_buta_cleaned}")

print(f"Użytkownik jest kobietą: {is_female}")
