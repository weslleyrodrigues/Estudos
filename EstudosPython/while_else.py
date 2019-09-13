'''
While / Else
contadores
acumuladores
'''
contador = 1
acumulador = 1

while contador<=10:
    print(contador,acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador +=1
else: #Executa quando o while for falso
    print('Cheguei no else')
print('Nao estou no Else pois o while nao deu False')