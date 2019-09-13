"""
Operadores relacionais
== igualdade
> maior
< menor
>= maior ou igual
<= menor ou ogual
!= diferente
"""

num1 = 2
num2 = 2
expressao = (num1 == num2)
print(expressao)

num3 = 3
num4 = 2
expressao2 = (num3>num4)
print(expressao)

var1 = 'Weslley'
var2 = 'Rodrigues'
expressao3 = (var1 != var2)
print(expressao3)

##
print()
nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
idade = int(idade)

#Limite para pegar emprestimo
idade_menor = 20 #muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <=idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} nao pode pegar o empréstimo')
