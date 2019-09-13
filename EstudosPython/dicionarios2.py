"""
Dicinario é um tipo de lista não ordenada onde cada elemento
esta associado a uma chave

- cada valor esta associado a um indice de numero inteiro
- CHave -> VALOR 
"""

# O Conjunto de elementos dicionário é representado por duas chaves
pessoa = {'nome':'Prof. Alberto','idade':43,'cursos':['React','Python']}
print(pessoa)

#Alterando dados
pessoa['idade'] = 44
pessoa['cursos'].append('Angular') #Estou adicionado um objeto a mais
print(pessoa)

#Retirando dados
pessoa.pop('idade') #Lê e retira o atributo
print(pessoa)

#Adicionando
pessoa.update({'idade':40,'sexo':'masculino'})
print(pessoa)

#Excluindo
del pessoa['cursos']
print(pessoa)

pessoa.clear() #Limpa tudo
print(pessoa)
