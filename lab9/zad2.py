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

print("Liga Mistrzow:", LigaMistrzow)
print("Liga Europy:", LigaEuropy)
print("Liga Konferencji:", LigaKonferencji)
print("Liga Narodow:", LigaNarodow)

intersection_me = LigaMistrzow.intersection(LigaEuropy)
intersection_mk = LigaMistrzow.intersection(LigaKonferencji)
intersection_mn = LigaMistrzow.intersection(LigaNarodow)
intersection_ek = LigaEuropy.intersection(LigaKonferencji)
intersection_en = LigaEuropy.intersection(LigaNarodow)
intersection_kn = LigaKonferencji.intersection(LigaNarodow)

print("\nCzesc wspolna:")
print("Liga Mistrzow i Liga Europy:", intersection_me)
print("Liga Mistrzow i Liga Konferencji:", intersection_mk)
print("Liga Mistrzow i Liga Narodow:", intersection_mn)
print("Liga Europy i Liga Konferencji:", intersection_ek)
print("Liga Europy i Liga Narodow:", intersection_en)
print("Liga Konferencji i Liga Narodow:", intersection_kn)

difference_me = LigaMistrzow.difference(LigaEuropy)
difference_mk = LigaMistrzow.difference(LigaKonferencji)
difference_mn = LigaMistrzow.difference(LigaNarodow)
difference_ek = LigaEuropy.difference(LigaKonferencji)
difference_en = LigaEuropy.difference(LigaNarodow)
difference_kn = LigaKonferencji.difference(LigaNarodow)

print("\nRoznica:")
print("Liga Mistrzow - Liga Europy:", difference_me)
print("Liga Mistrzow - Liga Konferencji:", difference_mk)
print("Liga Mistrzow - Liga Narodow:", difference_mn)
print("Liga Europy - Liga Konferencji:", difference_ek)
print("Liga Europy - Liga Narodow:", difference_en)
print("Liga Konferencji - Liga Narodow:", difference_kn)

union_me = LigaMistrzow.union(LigaEuropy)
union_mk = LigaMistrzow.union(LigaKonferencji)
union_mn = LigaMistrzow.union(LigaNarodow)
union_ek = LigaEuropy.union(LigaKonferencji)
union_en = LigaEuropy.union(LigaNarodow)
union_kn = LigaKonferencji.union(LigaNarodow)

print("\nSuma:")
print("Liga Mistrzow + Liga Europy:", union_me)
print("Liga Mistrzow + Liga Konferencji:", union_mk)
print("Liga Mistrzow + Liga Narodow:", union_mn)
print("Liga Europy + Liga Konferencji:", union_ek)
print("Liga Europy + Liga Narodów:", union_en)
print("Liga Konferencji + Liga Narodow:", union_kn)

issuperset_me = LigaMistrzow.issuperset(LigaEuropy)
issuperset_mk = LigaMistrzow.issuperset(LigaKonferencji)
issuperset_mn = LigaMistrzow.issuperset(LigaNarodow)
issuperset_ek = LigaEuropy.issuperset(LigaKonferencji)
issuperset_en = LigaEuropy.issuperset(LigaNarodow)
issuperset_kn = LigaKonferencji.issuperset(LigaNarodow)

print("\nCzy zawiera podzbior:")
print("Liga Mistrzow zawiera Ligę Europy:", issuperset_me)
print("Liga Mistrzow zawiera Ligę Konferencji:", issuperset_mk)
print("Liga Mistrzow zawiera Ligę Narodów:", issuperset_mn)
print("Liga Europy zawiera Ligę Konferencji:", issuperset_ek)
print("Liga Europy zawiera Ligę Narodow:", issuperset_en)
print("Liga Konferencji zawiera Ligę Narodow:", issuperset_kn)

issubset_me = LigaMistrzow.issubset(LigaEuropy)
issubset_mk = LigaMistrzow.issubset(LigaKonferencji)
issubset_mn = LigaMistrzow.issubset(LigaNarodow)
issubset_ek = LigaEuropy.issubset(LigaKonferencji)
issubset_en = LigaEuropy.issubset(LigaNarodow)
issubset_kn = LigaKonferencji.issubset(LigaNarodow)

print("\nCzy jest podzbiorem:")
print("Liga Mistrzow jest podzbiorem Ligi Europy:", issubset_me)
print("Liga Mistrzow jest podzbiorem Ligi Konferencji:", issubset_mk)
print("Liga Mistrzow jest podzbiorem Ligi Narodów:", issubset_mn)
print("Liga Europy jest podzbiorem Ligi Konferencji:", issubset_ek)
print("Liga Europy jest podzbiorem Ligi Narodow:", issubset_en)
print("Liga Konferencji jest podzbiorem Ligi Narodow:", issubset_kn)
