import requests

print('####################')
print('### Cunsulta CEP ###')
print('####################\n')


x=0
opcoes = int(input("Quantos CEP's deseja consultar? "))


def retorne_endereco(cep):
    global x
    if len(cep) != 8:
        print('Quantidade de digitos inválido!')
        exit()
        
    requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = requisicao.json()
    
    #Quando o cep nao é encontrado a Api retorna um 'erro', sendo assim, fazemos o tratamento da mesma
    if 'erro' not in requisicao.json():
        #print(requisicao.json())  Dessa forma exibo o json extraido
        out = '''
            CEP: {} | {}
            Bairro: {}
            Cidade: {}
            '''.format(endereco['cep'],endereco['logradouro'],endereco['bairro'], endereco['uf'])
        return out
    else:
        print('O CEP digitado não foi encotrado ou é inválido')
    x += 1

while x < opcoes:
    cep=input('Digite seu CEP: ')
    resultado = retorne_endereco(cep)
    print(resultado)
    
print('acabou')
