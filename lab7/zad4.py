
krotka = ("pierwszy", "drugi", "trzeci", "czwarty", "piaty", "szosty")
slowo = input("Podaj słowo do wyszukania: ")

if slowo in krotka:
    indeks = krotka.index(slowo)
    print(f"Slowo '{slowo}' znajduje sie w krotce na indeksie {indeks}.")
else:
    print(f"Slowo '{slowo}' nie znajduje sie w krotce.")

dluzszy_tekst = ' '.join(krotka) + " cos tam cos tam cost tam latataa"

wystapienia = dluzszy_tekst.count(slowo)
if wystapienia > 0:
    print(f"Słowo '{slowo}' znajduje się w tekscie {wystapienia} razy.")
else:
    print(f"Słowo '{slowo}' nie znajduje sie w dluzszym tekscie.")
