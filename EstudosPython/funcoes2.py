# Função com retorno
print("Exemplo 1")
def soma(numero1,numero2):
    resposta = numero1 + numero2
    return resposta
    
print(soma(5,5))
## ou
retorno = soma(5,5)
print(retorno)

print("\nExemplo 2")
def itens(palavras):
    if len(palavras) ==7:
        return True
    else:
        return False
        
print(itens('alface'))

 

# Função sem retorno
print("\nExemplo 3")
def imprimir():
    print('oi')

imprimir() #chamando a função
