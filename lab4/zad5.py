sum = 0
count_of_input_numbers = 0
avg = 0

while True:
    number = int(input("Wprowadz liczbe: "))
    count_of_input_numbers += 1
    sum += number
    avg = sum/count_of_input_numbers
    if(sum > 200 or avg == 66):
        print("warunek spelniony")
        break