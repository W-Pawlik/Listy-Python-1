

print("Jakie wartosci chcesz zliczac?")
print("1-int")
print("2-float")
choice = int(input("Wprowadz wybor: "))
n = int(input("Wprowadz ilosc liczb calkowitych: "))
i = 0
sum = 0
while i != n:
    match choice:
        case 1:
            number = int(input(f'{i+1} liczba: '))
            if(number<0):
                i +=1
                continue
            sum += number
            avg = sum/(i+1)
            i += 1
        case 2:
            number = float(input(f'{i+1} liczba: '))
            if(number<0):
                i+=1
                continue
            sum += number
            avg = sum/(i+1)
            i += 1
        case _:
            print("Zla liczba")
            break
    print(avg)