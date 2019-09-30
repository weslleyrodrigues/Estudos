"""
Nexte exemplo, desejo pegar a primeira coluna do csv e verificar se há valores com
menos de 4 caracters
"""

import csv

with open('teste.csv','r') as entrada: #a letra r é de read - leitura
    arquivo_csv = csv.reader(entrada) #armazeno o arquivo csv em uma variavel
    next(arquivo_csv) #Pula a primeira linha (do cabeçalho)
    IDS = []
    log = []
    indice = 2
    for item in arquivo_csv:
        IDS.append(item[0])
      
    for valor in IDS:
        qtd_caracters=len(valor)
        if qtd_caracters < 4:
            log.append(str(indice))
            indice +=1
        else:
            print('[{}] - {}'.format(indice,valor))
            indice +=1
    
    print('Há problemas nos índices: ' + ', '.join(log) + '. Favor verificar.')
    