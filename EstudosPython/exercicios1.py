"""
Faça um programa que peça aos usuários para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

numero = input('Digite um numero: ')
# isdigit - Como pode ser percebido, esta função retornou true apenas quando a string era inteiramente composta por números. Qualquer coisa diferente de 0,1,2,3,4,5,6,7,8 e 9 retorna falso. 
if not numero.isdigit():
    print('isso não é um número inteiro: ')
else:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é PAR')
    else:
        print(f'{numero} é IMPAR')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario descrito, exiba a saudação apropriada. EX:
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
'''
hora = input('Que horas são (0 a 24): ')

if hora.isdigit():
    hora = int(hora)
    if hora<0 or hora >23:
        print('O horario deve estar entre 0 e 23')
    else:
        if hora>=0 and hora <=11:
            print("Bom dia!")
        elif hora>=12 and hora<=17:
            print("Boa tarde!")
        elif hora>=18 and hora<=23:
            print('Boa noite!')
else:
    print('Valor inválido')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; Maior que 6 escreva "Seu nome é muito grande".
'''
nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <=4:
    print('Seu nome é curto')
elif tamanho <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')