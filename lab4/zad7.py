number = int(input("Wprowadz liczbe: "))

if number > 1:
    if number == 2:
        print(f'{number} jest liczba pierwsza')
    else:
        for i in range(2, number):
            if (number%i!=0 or number==2):
                print(f'{number} jest liczba pierwsza')
                break
            else:
                print(f'{number} nie jest liczba pierwsza')
                break
else:
    print(f'{number} nie jest liczba pierwsza, jest ujemna lub rowna 1')