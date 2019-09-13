"""
Crie uma função1 que recebe uma funçao2 como parametro e retorne o valor da função2 executada
"""
def func1(valor):
    return valor
    
def func2(valor):
    return valor
    
valor = func2(5)
    
print(func1(valor))

## ou
print()
def ola_mundo():
    return "olá mundo!!"
def mestre(funcao):
    return funcao()
    
resultado=mestre(ola_mundo)
print(resultado)

"""
Crie uma função1 que recebe uma funçao2 como parametro e retorne o valor da função2 executada. Faça a função 1 executar duas funções que recebam um numero diferente de argumentos
"""
print("###############")
def funcao1(x,y):
    return x,y
    
def funcao2(numero1):
    return numero1
x = funcao2(5)

def funcao3(numero3):
    return numero3
y = funcao3(10)

print(func1(x),(y))

#ou
print()
def mestre(funcao, *args,**kwargs):
    return funcao(*args,**kwargs)

def fala_oi(nome):
    return  'oi {}'.format(nome)

def saudacao(nome,saudacao):
    return '{} {}'.format(nome,saudacao)

resultado = mestre(fala_oi,'weslley')
print(resultado)
resultado2 = mestre(saudacao,'weslley','bem vindo')
print(resultado2)