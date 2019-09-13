"""
For/Else em python
"""

variavel = ['Weslley','Joao','Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'): #Converte a palavra para minusculo(lower) e verifica a primeira letra(startswith)
        comeca_com_j = True
if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J')

# ou #
print()
for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J')