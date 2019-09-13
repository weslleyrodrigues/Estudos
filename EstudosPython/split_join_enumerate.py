"""
Split, Join, Enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista # list # Iteraveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1 = string.split(' ') #Separa os valores pelo espaço
print(lista1)

lista2 = string.split(',') #Separa os valores pela virgula.
print(lista2)

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes>contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é ***{palavra}***({contagem}x)') 

#Removendo espaço e colocando a primeira letra como maiuscula
print()
for valor in lista2:
    print(valor.strip().capitalize())

### JOIN ####

print()
string = 'O Brasil é penta'
lista = string.split(' ')
string2 = ','.join(lista) #Neste caso eu juntei os elementos da lista com a virgula
print(string2)

print()
string2 = ' '.join(lista) #Estrou juntando os elementos separando por espaço (como estava antes)
print(string2)


### Enumerate ###
print()
for indice, valor in enumerate(lista):
    print(indice,valor)

print()
### lista dentro de outra lista ###
# A forma como o enumerate funciona
lista = [
    [1,'Luiz'],
    [2,'Joao'],
    [3,'Maria'],
]
for v in lista:
    print(v[0],v[1])

## desempacotando
print()
lista = ['Luiz','Joao','Maria']
for indice, nome in enumerate(lista):
    print(indice,nome)

## desempacotando
print()
lista = ['Luiz','Joao','Maria']
n1,n2,n3 = lista
print(n2)
