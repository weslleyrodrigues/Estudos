"""
Tipos de dados:
str - string - textos 'assim' e "assim"

int - inteiro - 123456 0 -10 -4 -122

float - real/ponto flutuante - 10.50 1.5 -10.10

bool - booleano/lógico - True/False 10 == 10

"""

print('Weslley', type('Weslley'))
print('10', type('10')) #considera como string pois esta em aspas
print(10, type(10))
print(25.25, type(25.25))
print(10 == 10, type(10==10))
print('L' == 'l', type('L' == 'l'))
print(bool('')) #como nao tem valor ou é uma string vazia, para comparar, ele avalia em falso

#Converter um tipo para outro tipo - Casting
#Muda de String para booleano
print('Weslley', type('Weslley'), bool('Weslley'))

#convertendo string para tipo
print('10', type('10'), type(int('10')))
print('Weslley', type(float(10.5)))

#type serve para mostrar o tipo

#String: nome
print('Weslley', type('Weslley'))

#Idade: Int
print('21', type(21))

#Altura: float
print('1.80', type(1.80))

#É maior de idade 10 > 20
print('21>18', type(21>18))
