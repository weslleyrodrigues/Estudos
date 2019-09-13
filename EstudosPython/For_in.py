'''
For in em python
Iterando String com For
Função range (start=0, stop, step=1)
'''

nomes = ['weslley','joao','jose']
for n in nomes:
    print(n)
else:
    print('Todos os nomes foram listados')
    
##########

texto = 'python'

c=0
while c < len(texto):
    print(texto[c]) #Acessando o Indice da minha String
    c += 1

print('#########  COM FOR  ###########')
#Com FOR

texto2 = 'PythonFOR'
for letra in texto2:
    print(letra)

print('#########  Range  ###########')
for numero in range(10): #Numero é a variavel que eu determinei como o nome que eu quiser
    print(numero) #Neste caso sera impresso de zero a nove, pois como nao especifiquei o inicio

print('#########  Range ex2  ###########')
for numero in range(5,10,1): #Neste caso, começa a contar a partir do numero 5 ate o indice 10, contando de 1 em 1
    print(numero)

print('#########  Range ex3 ###########')
for numero in range(5,10,2): #Neste caso, começa a contar a partir do numero 5 ate o indice 10, contando de 2 em 2
    print(numero)

print('#########  Range ex4 - Decremento ###########')
for numero in range(20,9,-1):
    print(numero)

print('#########  Range ex5 - Multiplo ###########')
for numero in range(0,100,8): #Estou trazendo os multiplos de 8
    print(numero)

print('Ou dessa forma:')

for numero in range(100):
    if numero%8 == 0:
        print(numero)

print('')
#Alterando maiusculo dentro da minha string
texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

print('')
#Pulando uma letra
texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue #Pula para a proxima sequencia 
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)