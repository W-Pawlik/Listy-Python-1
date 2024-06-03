
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)



def main():

    print("1 - Kalkulator liczby dziesietnej")
    print("2 - Kalkulator liczby binarnej")
    print("3 - Kalkulator liczby szesnastkowej")
    choice = int(input("Wybierz liczbe: "))

    match choice:
        case 1:
            decimal = int(input("Podaj liczbę dziesiętną: "))
            print(f"Liczba binarna: {decimal_to_binary(decimal)}")
            print(f"Liczba ósemkowa: {decimal_to_octal(decimal)}")
            print(f"Liczba szesnastkowa: {decimal_to_hexadecimal(decimal)}")
        case 2:
            binary = input("\nPodaj liczbę binarną: ")
            print(f"Liczba szesnastkowa: {binary_to_hexadecimal(binary)}")
            print(f"Liczba ósemkowa: {binary_to_octal(binary)}")
        case 3:
            hexadecimal = input("\nPodaj liczbę szesnastkową: ")
            print(f"Liczba ósemkowa: {hexadecimal_to_octal(hexadecimal)}")
        case _:
            print("Zly numer")


if __name__ == "__main__":
    main()
