"""
Nas tuplas eu nao posso editar, excuir e adicionar elementos
AS TUPLAS PODEM SER CRIADAS SEM PARENTESES, VAZIA OU COM 1 ELEMENTO
"""
t1 = (1,2,3,4,'a','weslley')
print(type(t1))
t2 = () # Vazio é uma tupla

print(type(t2))
t3 = 1, # se eu colocar uma virgula, ela se torna uma tupla
print(type(t3))


#Ver cada elemento da tupla
for cont in t1:
    print(cont,type(cont))
    
#Fatiar
print(t1[2:]) #pega do elemento 2 ao ultimo

#Unir duas tuplas
a = 1,2,3
b = 4,5,6
c = a+b
print(c)

#Multiplicar a tupla varias vezes 
teste = (1,2,3,4,'amanda','w') * 5
print(teste)

#Editando um valor da tupla
Tupla = (1,2,3,4,5)
Tupla = list(Tupla) #Converto em lista
Tupla[1] = 10 #Edito o valor do indice 1
print (Tupla)
#Caso eu queira voltar a variavel a ser uma tupla
Tupla = tuple(Tupla)
