'''
Iterando Strings com while em python
'''
#String é imutavel, nao consigo alterar um valor dentro dela, apenas o valor da variavel
minha_string = 'Weslley Rodrigues de Sousa Pereira'
print(minha_string[1]) #Exibe a letra E
#Exibe cada letra em uma linha
tamanho_string = len(minha_string)
c = 0
while c < tamanho_string:
    print(c, minha_string[c])
    c +=1
####

### Mostrando os R maiusculos
c = 0
nova_string = ''
while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string = nova_string + minha_string[c]
    c +=1
print(nova_string)

print('A letra R apareceu ', minha_string.count('r'),'vezes')

#############
print()

while True:
    minha_string = input('Digite uma frase:')
    tamanho_string = len(minha_string)
    
    c=0
    contagem_atual = 0
    letra = ''
    while c < tamanho_string:
        qtd_vezes_letra = minha_string.count(minha_string[c])

        if contagem_atual < qtd_vezes_letra and minha_string[c].strip(): #.strip retira os espaços
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra
        #print(minha_string[c], conta)
        c += 1
    print(letra, contagem_atual)
