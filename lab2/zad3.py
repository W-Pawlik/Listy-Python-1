a = int(input("Wprowadz liczbe a: "))
b = int(input("Wprowadz liczbe b: "))
c = int(input("Wprowadz liczbe c: "))

if(a!=b and a!=c and b!=c):
    if(a>b and a>c):
        if(b>c):
            print("a>b>c")
        elif(c>b):
            print("a>c>b")
        elif(b==c):
            print("a> b=c")
    elif(b>a and b>c):
        if(a>c):
            print("b>a>c")
        elif(c>a):
            print("b>c>a")
        elif(a==c):
            print("b> a=c")
    elif(c>a and c>b):
        if(b>a):
            print("c>a>b")
        elif(a>b):
            print("c>a>b")
        elif(b==a):
            print("c>b=a")
else:
    print("Liczby sa identyczne")