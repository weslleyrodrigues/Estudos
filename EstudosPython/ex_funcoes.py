"""
- Crie uma função que exibe uma saudação com os parametros saudação e nome
"""
def saudacao(msg,nome):
    return '{} {}'.format(msg,nome)
resposta=saudacao('ola','weslley')
print(resposta)

##ou
def saudacao2(msg,nome):
    print('{} {}'.format(msg,nome))
saudacao2('ola novamente','weslleyy')

print()
"""
- Crie uma função que recebe tres numeros com parametros e exiba a soma entre eles
"""
def soma(n1,n2,n3):
    return n1+n2+n3
resultado=(soma(5,5,5))
print(resultado)

##ou

def soma2(n1,n2,n3):
    print(n1+n2+n3)
soma2(5,5,5)

print()
"""
- Crie uma função que receba dois números. O primeiro é o valor e o segundo um percentual
(Ex. 10%). Retorne o valor do primeiro numero somado do aumento do percentua do mesmo
"""

def percentual(n1,n2):
    resultado = (n1*n2)/100 + n1 # ou (n1+(n1*n2/100))
    return resultado
result = percentual(5,50)
print(result)   

print()
"""
Fizz - Buzz - Se o parametro da função for divisivel por 2, retorne Fizz, se o parametro da 
função for divisivel por 5, retorne Buzz. Se o parametro da função por divisivel por 5 e por 3
retorne FizzBuzz, caso contrario retorne o numero enviado
"""

def fizzbuzz(numero):
    if numero/3 in range(0,1000,3):
        return "Fizz"
    elif numero/5 in range(0,1000,3) and numero/3 in range(0,1000,5):
        return "FizzBuzz"
    elif numero/5 in range(0,1000,5):
        return "Buzz"
    else:
        return numero
        
resultado = fizzbuzz(9)
print(resultado) 

# ou
print()
def fizzbuzz2(numero):
    if numero%3 == 0 and numero%3 == 0:
        return ('FizzBuzz - {} é divisivel por 3 e 5'.format(numero))
    if numero%3 == 0:
        return('Fizz - {} é divisivel por 3'.format(numero))
    if numero%5 == 0:
        return('Buzz - {} é divisivel por 5'.format(numero))
    return numero

#print(fizzbuzz2(8))

from random import randint
for i in range(10):
    aleatorio = randint(0,10)
    print(fizzbuzz2(aleatorio))

#



