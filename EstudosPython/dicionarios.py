"""
Dicinario é um tipo de lista não ordenada onde cada elemento
esta associado a uma chave

- cada valor esta associado a um indice de numero inteiro
- CHave -> VALOR 
"""

# O Conjunto de elementos dicionário é representado por duas chaves
print(type ({}) )

d1 = {}
print('d1 tem o tipo: ',type(d1))
#Adicionando valores
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

#ou
print()
d1 = dict(chave1='valor da chave',chave2='valor da outra chave')
print(d1)


"""
As chaves devem conter um unico valor
se repetir o valor da chave, o mesmo sera sobreposto
exemplo -  chave = {'valor':500,'valor':700} - como ambos tem o msm valor
o ultimo inserido vai sobrepor, valor contera 700
"""

# 
print()

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))

# Exemplo abaixo - Caso nao tiver o valor, traz um valor dafault (no caso vazil)
print()
print(pessoa.get('tags'),[])
