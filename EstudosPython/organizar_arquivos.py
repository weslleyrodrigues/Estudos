import os
import shutil

arquivos = os.listdir('/home/weslley_pereira/Estudos/EstudosPython')
print(type(arquivos))

resposta = input('O que deseja fazer? \n [1] - Criar pastas \n [2] - Mover os arquivos \n [0] - Sair \n')

def validar (resposta):
    resposta = int(resposta)
    if resposta == 1:
        # print('VC ta criando.. ')
        for x,y in enumerate(arquivos):
            os.mkdir(arquivos[x].strip('.py'))
    elif resposta == 2:
        for x,y in enumerate(arquivos):
            if arquivos[x]:
                shutil.move(arquivos[x],arquivos[x].strip('.py'))
    elif resposta == 0:
        pass
try:
    validar(resposta)
except ValueError:
    while True:p
        validar(resposta)
        break
    
# for x,y in enumerate(arquivos):
#     #os.mkdir(arquivos[x].strip('.py'))
#     if arquivos[x]:
#         shutil.move(arquivos[x],arquivos[x].strip('.py'))

