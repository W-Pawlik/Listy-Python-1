
min_safe_altitude_km = 5
min_safe_altitude_meters = min_safe_altitude_km * 1000

altitude_meters = int(input("Na jakiej wysokosci lecimy? [w metrach]: "))

# Sprawdzenie, czy wysokość jest poniżej 5 km
if altitude_meters < min_safe_altitude_meters:
    print(f"{altitude_meters / 1000:.2f} km to za nisko!")
else:
    print("Na tej wysokosci jestes już bezpieczny.")
