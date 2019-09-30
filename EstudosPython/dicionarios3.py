d1 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'tupla',
}

#Trazer as chaves
for chave in d1:
    print(chave)
    
print()

#Trazer os valores
for valores in d1.values():
    print(valores)
    
print()    
    
#Trazer a chave e valor
for k in d1.items():
    print(k[0],k[1])
   
print()
    
#ou
for k,v in d1.items():
    print(k,v)
    
#### Dicionario dentro de outro ####
print()

clientes = {
    'cliente1' : {
        'nome':'weslley',
        'sobrenome':'Rodrigues',
    },
    'cliente2' : {
        'nome':'João',
        'sobrenome':'Pereira',
    },
    'cliente3' : {
        'nome':'Maria',
        'sobrenome':'Jose',
    },
        
}

for clientes_k,clientes_v in clientes.items():
    print('Exibindo {}'.format(clientes_k))
    for dados_k,dados_v in clientes_v.items():
        print('\t{} = {}'.format(dados_k,dados_v))
        
'''
Ao tentar atribuir um dicionario a uma variavel (na inteção de copia-lá)
Não dará certo pois é criada apenas uma 'referencia'
exemplo:
'''
print()

dicionario = {1:'a',2:'b',3:'c','d':['weslley','rodrigues']}
dicionario2 = dicionario

dicionario2[1] = 'XX'

print(dicionario)
print(dicionario2)

'''
Para fazer uma copia deve importar a bilbioteca 'copy' e usar os parametros 
'copy.deepcopy'
exemplo:
'''
print()

import copy
dic = {1:'a',2:'b',3:'c','d':['weslley','rodrigues']}
dic2 = copy.deepcopy(dic)

dic2[3] = 'teste'
dic[2] = 'terra'
print(dic)
print(dic2)

'''
Convertendo em Dicionario
'''
print()

lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3],
    ]
d1 = dict(lista)
print(d1)

#ou 
print()
lista2 = (
    ('c4',4),
    ('c5',5),
    ('c6',6),
    )
d2 = dict(lista2)
print(d2)

# Concatenando dicionarios
print()
d1.update(dicionario)
print(d1)