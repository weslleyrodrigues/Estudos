import requests

print('####################')
print('### Cunsulta CEP ###')
print('####################\n')

## Inicio
import logging
import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()
## Termino

opcoes = input("Quantos CEP's deseja consultar? ")
opcoes = int(opcoes)

x=0

while x < opcoes:
    
    cep=input('Digite seu CEP: ')
    
    if len(cep) != 8:
        print('Quantidade de digitos inválido!')
        exit()
        
    requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = requisicao.json()
    
    #Quando o cep nao é encontrado a Api retorna um 'erro', sendo assim, fazemos o tratamento da mesma
    if 'erro' not in requisicao.json():
        #print(requisicao.json())  Dessa forma exibo o json extraido
        print('CEP: {} | {}'.format(endereco['cep'],endereco['logradouro']))
        print('Bairro: {}'.format(endereco['bairro']))
        print('Cidade: {}'.format(endereco['uf']))
        print()
    else:
        print('O CEP digitado não foi encotrado ou é inválido')
        logging.warn('Todos os registros foram eviados com sucesso! hahahaehehuee')
    x += 1  
    
print('acabou')