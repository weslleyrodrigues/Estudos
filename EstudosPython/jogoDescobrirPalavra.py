secreto = 'perfume'
letras_digitadas = []
chances = 3

while True:
    if chances <=0:
        print('Você perdeu!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1: #vai validar se estou digitando apenas uma letra
        print('Ahhh isso não vale, digite apenas 1 letra por vez')
        continue
    letras_digitadas.append(letra) #Tudo o que for digitado seja incrementando na lista

    if letra in secreto:
        print(f'Uhuul, a letra "{letra}" existe na palavra secreta!!')
    else:
        print(f'Poxa vida.. A letra "{letra}" não existe na palavra secreta :(')
        letras_digitadas.pop() #Se a letra não conter na palavra secreta, o pop vai excluir o valor digitado da lista, deixando apenas as letras validas
    
    #Faz a validação
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in letras_digitadas:
            secreto_temporario +=letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print('Que legal!! Você ganhou!!')
        print(f'A palavra era **{secreto_temporario}**')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -=1 #faz o decremento das chances
    print(f'Você ainda tem {chances} chances.')    
    print()

