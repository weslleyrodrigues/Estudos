"""
Operador ternário
"""
logged_user = False
msg = 'Usuario Logado!' if logged_user else 'Usuario precisa logar'
print(msg)

print()

idade = input('qual sua idade? ')

if not idade.isnumeric():
  print('Voce precisa digitar numero')
else:
  idade = int(idade)
  e_de_maior = (idade>=18)
  msg= 'pode acessar' if e_de_maior else 'não pode acessar'
  print(msg)