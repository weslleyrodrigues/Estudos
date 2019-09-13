"""
*Criar variaveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Weslley Rodrigues'
idade = 21
altura = 1.80
peso = 60.0
ano = 2019

imc = peso/altura**2
data_nascimento = 2019-21

print(f'{nome} tem {idade} anos de idade, pesa {peso} Kg nasceu em {data_nascimento} e tem IMC {imc:.2f}')
