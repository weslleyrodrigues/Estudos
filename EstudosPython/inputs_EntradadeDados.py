nome = input ('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
print(f'O usuario digitou {nome} e o tipo da variavel é:'f'{type(nome)}')

print(f'O usuario digitou {idade} e o tipo da variavel é:'f'{type(idade)}')

## A função Input sempre retorna uma String, independente se eu digitei um número inteiro

ano_nascimento = 2019 - int(idade) #Estou fazendo um Casting, convertendo a string para inteiro

print()
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {ano_nascimento}.')

#EXEMPLO 2
print()
numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')
print("Dessa forma estou concatenando pois todo input retorna uma string: ", numero1 + numero2)

#forma correta
print()
numero3 = int(input('Digite o terceiro numero: '))
#ou
#Converto a variavel para inteiro
numero4 = input('Digite o quarto numero: ')
numero4 = int(numero4)

print('Dessa forma estou somando, pois converti os numeros para inteiro: ',numero3+numero4)
