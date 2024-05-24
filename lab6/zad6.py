import random

min = int(input("Wprowadz min zakresu: "))
max = int(input("Wprowadz max zakresu: "))
count = int(input("Wprowadz ilosc elementow listy: "))

tab = []
for element in range(0, count):
    element = random.randint(min,max)

    tab.append(element)
    print(f'Element tab: {element}')

    for el_tab in tab:
        if tab.count(el_tab)>1:
            tab.remove(el_tab)

    
print(tab)
print(len(tab))
