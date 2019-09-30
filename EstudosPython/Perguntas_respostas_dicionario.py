perguntas = {
    'Pergunta 1' : {
        'pergunta':'quanto é 2+2',
        'resposta':{'a':1,'b':4,'c':2},
        'resposta_certa':'b',
    },
    'Pergunta 2' : {
        'pergunta':'Quanto é 3*6',
        'resposta':{'a':12,'b':1,'c':18},
        'resposta_certa':'c',
    },
    'Pergunta 3' : {
        'pergunta':'Quanto é 5*5',
        'resposta':{'a':25,'b':95,'c':35},
        'resposta_certa':'a'
    }
}

resposta_certas = 0

for pk,pv in perguntas.items():
    print('{} : {}'.format(pk,pv['pergunta']))
    print('Respostas: ')
    for rk,rv in pv['resposta'].items():
        print('[{}]: {}'.format(rk,rv))
    resposta_usuario = input('Sua resposta: ')
    print()
    
    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns, voce acertou!')
        resposta_certas +=1
    else:
        print('Voce Errou')
    print()
    
qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas/qtd_perguntas * 100

print('Voce acertou {} perguntas'.format(resposta_certas))
print('Porcentagem de acerto: {:.2f}%'.format(porcentagem_acerto))
    