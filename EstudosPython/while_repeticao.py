'''
While em Python

Utilizado para realizar ações enquanto uma condição for verdadeira..

requisitos: Entender condições e operadores
'''

'''
while True: #Loop infinito
    nome = input('Qual o seu nome?')
    print(f'Ola {nome}')
'''
x=0
while x <=10:
    print(x)
    x=x+1
print('Acabou') #Esse bloco é exibido quando a condição for falsa

print()

# Continue - faz com que as linhas posteriores nao sejam executadas, portanto, no exemplo abaixo o numero 3 não é executado 
y=0
while y < 10:
    if y == 3: #quando o Y for 3, ele soma 1
        y = y + 1 # e passa continua na proxima execução, imprimindo 4 
        continue

    print(y)
    y = y + 1
print('Acabou')

print()

# Break - Para o nosso codigo
z=0
while z<10:
    if z==3:
        z = z + 1
        break
    print(z)
    z = z + 1
print('Acabou')

print()

#Outro exemplo
x = 0 #Coluna
while x < 10:
    y = 0 #Linha
    while y < 5:
        print(f'({x},{y})')
        y +=1
    x += 1 # x = x + 1

print('Acabou')

#Calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        print('Voce saiu!')
        break
    #Checa se a variavel foi preenchida por numero
    if not num_1.isnumeric() or not num_2.isnumeric():
        print()
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador Inválido')