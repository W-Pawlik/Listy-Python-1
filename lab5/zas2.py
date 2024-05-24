x = int(input("Wprowadz min zakresu: "))
n = int(input("Wprowadz max zakresu: "))
count_of_numbers = 0
sum = 0
avg = 0

for i in range(x,x+6):
    print(i)
    count_of_numbers += 1
    sum = sum + i
    avg = sum/count_of_numbers
    
    


print(f'Min = ', x)
print(f'Max = ', x+6)
print(f'Srenia: ', avg)
