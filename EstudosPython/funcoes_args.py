"""
Funções (def) em Python - *args **kwargs
"""
### entendendo o funcionamento
lista = [1,2,3,4,5,6]
n1,n2,*n = lista #armazena 1 em n1, 2 em n2 e o restante da lista armazena na variave n, por conta do asterisco
print(n1,n2,n)
#Ou seja, com asterisco ele pega todos os argumentos

### Desenpacotando cada valor da lista
lista = [1,2,3,4,5]
print(*lista,sep='-') #Adicionando um separador por 

### outro exemplo
print()
def func(*args):
    print(args[0]) #acessando o primeiro
    print(args[-1]) #acessando o ultimo 
    print(len(args)) #conta a quantidade de argumentos passados
func(1,2,3,4,5,6)
# obs. Os valores da tupla nao podem ser alterados

# **kwargs - Argumentos nomeados

def func2(*args,**kwargs):
    print(args)
    print(kwargs['nome'],kwargs['sobrenome'])
    #ou
    idade = kwargs.get('idade') #recomendavel usar get pois caso o argumento nao exista o programa retornará um erro
    
    #Fazendo a verificação
    if idade is not None:
        print (idade)
    print('Idade não existe')
    
lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]
func2(*lista1,*lista2,nome='weslley',sobrenome='rodrigues')