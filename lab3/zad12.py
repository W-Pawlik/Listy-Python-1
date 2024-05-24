import random

zero = 0
one = 0

for i in range(0,50):
    los = random.randint(0,1)
    if(los == 0):
        zero += 1
        print("orzel")
    else:
        one += 1
        print("reszka")
    

print("Liczba orlow: ", zero)
print("Liczba reszek: ", one)