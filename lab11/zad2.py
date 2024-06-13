import math

celsius = float(input("Podaj temperature w stopniach Celsjusza: "))

fahrenheit = celsius * 9/5 + 32
print(f"Temperatura w stopniach Fahrenheita: {'+' if fahrenheit >= 0 else '-'}{abs(fahrenheit):.2f}°F")

if fahrenheit <= 32:
    print("Woda zamarza.")
elif fahrenheit >= 212:
    print("Woda wrze.")
else:
    print("Woda jest w stanie cieklym.")

kelvin = celsius + 273.15
print(f"Temperatura w Kelwinach: {kelvin:.2f}K")

fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
print(f"Temperatura w stopniach Celsjusza z Fahrenheita: {fahrenheit_to_celsius:.2f}°C")

kelvin_to_celsius = kelvin - 273.15
print(f"Temperatura w stopniach Celsjusza z Kelwinów: {kelvin_to_celsius:.2f}°C")

fahrenheit_to_kelvin = (fahrenheit - 32) * 5/9 + 273.15
print(f"Temperatura w Kelwinach z Fahrenheita: {fahrenheit_to_kelvin:.2f}K")

kelvin_to_fahrenheit = (kelvin - 273.15) * 9/5 + 32
print(f"Temperatura w stopniach Fahrenheita z Kelwinow: {kelvin_to_fahrenheit:.2f}°F")
