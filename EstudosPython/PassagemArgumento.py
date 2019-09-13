import sys
argumentos=sys.argv

def soma(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2
    
if argumentos[1] == 'soma':
    resposta = soma(float(argumentos[2]),float(argumentos[3]))
elif argumentos[1] == 'sub':
    resposta =sub(float(argumentos[2]),float(argumentos[3]))

print(resposta)

#exemplo ao rodar

#python3 PassagemArgumento.py soma 5 4
#python3 PassagemArgumento.py sub 5 4