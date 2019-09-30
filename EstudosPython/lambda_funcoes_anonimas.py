"""
Lambda
"""
def funcao(arg,arg2):
    return arg * arg2
var = funcao(2,2)
print(var)
############# os dois fazem a mesma coisa #########
a = lambda x,y : x * y # nao uso parenteses nem return, e anonima pois nao defino um nome
print(a(2,2))

#exemplo 2 - ordenando uma lista q esta dentro de outra lista
print() 

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8]
    ]
    
print(lista)
print('Ordenado')
def func(item):
    return item[1]
#sort ordena a lista
lista.sort(key=func)
print(lista)

#exemplo 3 - Ordenando a lista usando lambda (simplificada)
print()
lista2 = [
    ['p1',13],
    ['p2',3],
    ['p3',8],
    ['p4',1],
    ['p5',4]
]
lista2.sort(key=lambda item:item[1], reverse=True) #reverse inverte a ordem
print(lista2)
