a = int(input("Wprowadz bok a: "))
b = int(input("Wprowadz bok b: "))
c = int(input("Wprowadz bok c: "))

if(a**2+b**2==c**2 or a**2+c**2==b or b**2+c**2==a):
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")
