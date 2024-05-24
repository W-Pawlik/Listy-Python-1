placa = 3891
kwota_odkladana = 333
i = 0
suma = 0
while i<12:
    suma = suma + kwota_odkladana + 0.08 * suma
    print(f'W {i+1} miesiacu pracownik odlozyl {suma}')
    i +=1
print(f'Ostatczeni zaoszczedzil {suma}')