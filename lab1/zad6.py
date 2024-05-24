dystans1_km = 30
czas1_min = 15

czas1_godzina = czas1_min / 60  
predkosc1_km_h = dystans1_km / czas1_godzina

print("Średnia prędkość dla pierwszego dystansu:", predkosc1_km_h, "km/h")

czas2_min = 12

czas2_godzina = czas2_min / 60  
predkosc2_km_h = dystans1_km / czas2_godzina

print("Średnia prędkość dla drugiego dystansu:", predkosc2_km_h, "km/h")

caly_dystans_km = 2 * dystans1_km  
caly_czas_godzina = (czas1_min + czas2_min) / 60  
predkosc_caly_dystans_km_h = caly_dystans_km / caly_czas_godzina

print("Średnia prędkość dla całego dystansu:", predkosc_caly_dystans_km_h, "km/h")

roznica_predkosci = abs(predkosc1_km_h - predkosc2_km_h)
print("Różnica w średniej prędkości między pierwszym a drugim dystansem:", roznica_predkosci, "km/h")
