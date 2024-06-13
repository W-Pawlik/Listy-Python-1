
feet = int(input("Podaj liczbę stop: "))
inches = int(input("Podaj liczbe cali: "))

total_inches = feet * 12 + inches

meters = total_inches * 0.0254
centimeters = total_inches * 2.54
millimeters = total_inches * 25.4
kilometers = total_inches * 0.0000254

yards = total_inches / 36
miles = total_inches / 63360
cubits = total_inches / 18
hands = total_inches / 4

print(f"\nWysokosc w metrach: {meters:.4f} m")
print(f"Wysokosc w centymetrach: {centimeters:.2f} cm")
print(f"Wysokosc w milimetrach: {millimeters:.2f} mm")
print(f"Wysokośscw kilometrach: {kilometers:.6f} km")

print(f"\nWysokosc w jardach: {yards:.4f} yd")
print(f"Wysokosc w milach: {miles:.8f} mi")
print(f"Wysokosc w lokciach: {cubits:.4f} cubits")
print(f"Wysokosc dloniach konskich: {hands:.2f} hands")
