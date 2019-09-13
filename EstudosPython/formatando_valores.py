"""
Formatando valores com modificadores 

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1/num_2

print('num_1') #se eu coloco desas forma a minha variavel é exibida

print('{:.2f}'.format(divisao)) #Deixo apenas duas casas decimais
## ou
print(f'{divisao:.2f}') #Realizo a mesma coisa

nome = 'Weslley Rodrigues'
print(f'{nome:s}') #estou dizendo que é uma string

#Quero que meu numero sejam preechidos por 10 casas de valor zero
valor1 = 1
print (f'{valor1:0>10}')

valor2 = 1150
print(f'{valor2:0>10}') #Sinal de menor adiciona os valores á esquerda
#Neste caso, como a variavel ja conte 4 valores, serão adicionados 6 casas de número zero.

print(f'{valor2:0^10}') # Estou adiconado o valor da minha variavel no centro e aplicando a quantidade de zeros no entorno do meu valor

print(f'{valor2:0<10}') #Estou adicionando o valor zero a minha direita
 
print(f'{valor2:.2f}') #Estrou transformando em float

print(f'{valor2:0>10.2f}')

nome = "weslley"
sobrenome = "Rodriges"
#Aplicando a strings
nome_formatado = '{n:#^15} {s:#^15}'.format(n=nome,s=sobrenome)
print(nome_formatado)

#Neste exemplo eu preencho o resto do meu nome com # até que dê 20 caracteres
nome = 'Lionel messi'
nome = nome.ljust(20,'#')
print(nome)
print()
nome = 'Lionel messi'
print(nome.lower())# tudo minisuculo
print(nome.upper())# tudo maiusculo
print(nome.title())# primeiras letras maiusculas