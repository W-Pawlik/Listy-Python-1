n = int(input("Wprowadz liczbe: "))

def lista_z_dzielnikow(n):
    tab = []
    for i in range(1,n+1):
        if n%i == 0:
            tab.append( i)
            i +=1
    return tab


print(lista_z_dzielnikow(n))