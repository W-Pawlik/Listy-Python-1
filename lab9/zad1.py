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
