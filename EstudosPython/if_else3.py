'''
Operadores logicos
AND 
OR
NOT
in e not in
'''
# (verdaderia e Verdadeiro) = Verdade
# (Verdadeiro e Falso) = Falso
#comparacao1 and comparacao2

#Verdadeiro ou Verdadeiro = Verdade
#Verdeiro ou Falso - Verdade
#comp1 or comp2

a = 2
b = 3

if not b>a: # o Not inverte o valor resultado (Nesse caso foi true, portanto retorna falso)
    print('B é maior do que A')
else:
    print('A é maior do que B')

# Também serve para checar se uma determinada variavel esta vazia, por exemplo:
print()
endereco = ''

if not endereco: #Se nome nao tiver nenhum valor ou for zero, executa o print
    print('Por favor, preencha o campo endereco')

# IN
print()
nome = 'Weslley Rodrigues'
if 'ley' in nome:
    print('Existe a letra ley na variavel nome')
else:
    print('Nao exsite o texto')

# checagem de usuario e senha, exemplo
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'weslley'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado no sistema')
else:
    print('Usuario ou senha incorretos')