"""
Listas em python
*Suporta varios valores, e de tipos diferentes*

fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#Exemplo:
# lista = [1,2,3,4,'Weslley',True,4.5] 

#Acessada por indices
#         0     1      2   3     4
lista = ['A','Bacana','C','D','10.5']
#      -  5   4   3   2   1

print(lista[1])
print(lista)
#Alterando valor do indice
lista[4]='Qualquer outra coisa'
print(lista[4])

#Fatiamento
print(lista[0:3])
print(lista[:3])#quando nao atribuo o primeiro valor ele entende como o primeiro indice
print(lista[2:])#peega os valores do indice 2 em diante

#ultimo indice da minha lista
print(lista[-1])

#salto de objetos de 2 em 2
print(lista[::2])

#de traz para frente
print(lista[::-1])

print()
##########---########
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l1)
print(l2)
print(l3)

print()
##########-Extend-########
l1.extend(l2)
print(l1)

print()
##########-Append-########
#Adiciona o valor no final da lista
l2.append('b')
print(l2)

print()
##########-Insert-########
#Insere o valor no indice 0 e passa os seguintes valores a diante
l2.insert(0,'Banana')
print(l2)

print()
##########-pop-########
#Deleta o ultimo item da lista
l2.pop()
print(l2)

print()
##########-del-########
#excluir valores dos indices
l2 = [1,2,3,4,5,6,7,8,9]
del(l2[3:5])
print(l2)

#ou
del(l2[0])
print(l2)

#Pegar o maior e menor valor:
#MAX E MIN
print(max(l2)) #maior valor
print(min(l2)) #Menor valor


#criando uma sequencia de numeros mais facil com o range
#Converter objetos iteraveis em uma lista
l2 = range(1,10) #objeto iteravel (usa o for para acessa-los)
print(l2)

#Crio uma lista de 1 a 10  (convertendo o objeto iteravel range)
l2 = list(range(1,10))
print(l2)

#Multiplos de 12 por exemplo
l2 = list(range(0,100,12)) #12 indica a sequencia de pulos
print(l2)

#visualizando cada elemento com o for
for valor in l2:
    print(valor)


print()
l2 = ['String',True,10,-20.5]
for elemento in l2:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')