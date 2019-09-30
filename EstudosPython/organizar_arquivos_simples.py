import os, sys
import shutil
import csv

# arquivos = os.listdir ('C:/Users/deploy/Desktop/migracao')
extensao = ['py', 'txt']
diretorio = os.path.dirname(os.path.abspath(__file__)) #pega o diretorio atual(path absoluto)
arquivos = os.listdir (diretorio)
print(arquivos)
temporario = ''
try:
    for x,y in enumerate(arquivos):
        temporario = arquivos[x].split('.')
        if temporario[-1] in set(extensao):
            temp = arquivos[x].strip('.' + temporario[-1])
            print(temp)
            os.chdir(diretorio)
            if temp == 'teste':
                print(temp)
                #print(diretorio+'/'+temporario)
                pass
            else:
                os.mkdir(temp)
                shutil.move(arquivos[x],diretorio+'/'+temp)
except FileExistsError:
    print('Arquivo ja existe.. ')

with open('users.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])