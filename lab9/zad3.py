import random

teams_pool = [
    "Real Madrid", "PSG", "Bayern Monachium", "Barcelona", "Juventus",
    "Liverpool", "Manchester City", "Chelsea", "Inter Mediolan", "AC Milan",
    "Atletico Madryt", "Borussia Dortmund", "Ajax", "Tottenham", "Arsenal",
    "Manchester United", "Sevilla", "Roma", "Napoli", "RB Leipzig"
]

LigaMistrzow = set(random.sample(teams_pool, 10))
LigaEuropy = set(random.sample(teams_pool, 10))
LigaKonferencji = set(random.sample(teams_pool, 10))
LigaNarodow = set(random.sample(teams_pool, 10))


print("\nDługość Liga Mistrzow:", len(LigaMistrzow))
print("Długość Liga Europy:", len(LigaEuropy))
print("Długość Liga Konferencji:", len(LigaKonferencji))
print("Długość Liga Narodow:", len(LigaNarodow))

common_elements = LigaMistrzow.intersection(LigaEuropy, LigaKonferencji, LigaNarodow)

for team in common_elements:
    LigaMistrzow.discard(team)
    LigaEuropy.discard(team)
    LigaKonferencji.discard(team)
    LigaNarodow.discard(team)

intersection_me = LigaMistrzow.intersection(LigaEuropy)
difference_me = LigaMistrzow.difference(LigaEuropy)
union_me = LigaMistrzow.union(LigaEuropy)
issuperset_me = LigaMistrzow.issuperset(LigaEuropy)
issubset_me = LigaMistrzow.issubset(LigaEuropy)

print("\nCzesc wspolna między Liga Mistrzów i Liga Europy:", intersection_me)
print("Roznica między Liga Mistrzow i Liga Europy:", difference_me)
print("Suma między Liga Mistrzow i Liga Europy:", union_me)
print("Liga Mistrzow zawiera Lige Europy:", issuperset_me)
print("Liga Mistrzow jest podzbiorem Ligi Europy:", issubset_me)

lista_LigaMistrzow = list(LigaMistrzow)
lista_LigaEuropy = list(LigaEuropy)
lista_LigaKonferencji = list(LigaKonferencji)
lista_LigaNarodow = list(LigaNarodow)

print("\nLista Liga Mistrzow:", lista_LigaMistrzow)
print("Lista Liga Europy:", lista_LigaEuropy)
print("Lista Liga Konferencji:", lista_LigaKonferencji)
print("Lista Liga Narodów:", lista_LigaNarodow)