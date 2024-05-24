max_number = int(input("Wprowadz zakres: "))
for i in range(max_number,0):
    if(i%6==0 and i%9==0):
        print(i)