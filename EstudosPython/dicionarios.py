"""
Dicinario é um tipo de lista não ordenada onde cada elemento
esta associado a uma chave

- cada valor esta associado a um indice de numero inteiro
- CHave -> VALOR 
"""

# O Conjunto de elementos dicionário é representado por duas chaves
print(type ({}))

d1 = {}
print('d1 tem o tipo: ',type(d1))
d1 ['aaa'] = 100
d1 ['bbb'] = 200
d1 ['ccc'] = 300
print(d1)

# OU
print()
pessoa = {'nome':'Weslley','idade':20,'cursos':['Portugues','Ingles']}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][0])
print(pessoa['cursos'][1])

# 
print()

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))

# Exemplo abaixo - Caso nao tiver o valor, traz um valor dafault (no caso vazil)
print()
print(pessoa.get('tags'),[])
