'''
Manipulando Strings
*String indices
*Fatiamento de strings (inicio:fim:passo)
*Funções built-in len, abs, type, print, etc..
Essas funções podem ser usadas diretamente em cada tipo
'''

#Indices POSITIVOS   [012345678]
texto =              'Python_S2'
#Indices NEGATIVOS  -[987654321]
print(texto[7]) #Apresenta a letra 'S'

nova_string = texto[2:6] #apresenta do indice 2 ao 5, pois o ultimo nao é incluido
print(nova_string)

print(texto[:6]) #Dessa forma imprimo do inicio ao quinto indice, pois quanto nao coloco o primeiro valor é entendivel como zero

print(texto[-9]) #Apresenta a letra P (primeiro indice)
print(texto[-9:-3]) #Apresenta Python
print(texto[-1]) #Apresenta o ultimo indice
print(texto[:-1]) #Imprimo tudo menos o ultimo indice

url = 'www.google.com.br/'
nova_url = url[:-1]
print(nova_url) #Imprime sem a barra final

#Vai do indice 0 ao 6 contando de 2 em 2
print(texto[0:6:2])

#Neste exemplo ele vai ate o final da string, pulando de tres em tres
print(texto[0::3])

#Contando o numero de caracters 
print(len(texto))