sum = 0
count_of_input_numbers = 0

while True:
    number = float(input("Wprowadz liczbe: "))
    print("Wpisana liczba: ", number)
    if number == 0:
        break
    else:
        sum += number
        count_of_input_numbers += 1
        print(f'Srednia {count_of_input_numbers} liczb wynosi: {sum/count_of_input_numbers}')