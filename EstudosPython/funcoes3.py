## exemplo 2

def saudacao(msg='ola',nome='usuario'): #defino valores dafault
    nome=nome.replace('e','3') #substitui a letra e pelo numero 3
    msg=msg.replace('e','3') #substitui a letra e pelo numero 3
    print(msg,nome)
    
saudacao(nome='luiz',msg='olaaa!') #independente da ordem, a mesma sera exibida conforme especifiquei na funçao
saudacao('oi','luiz')
saudacao() #exibe o valor padrao que defini 

# com return
def saudacao(msg='ola',nome='usuario'):
    return ('{} {}').format(msg,nome)
    
variavel = saudacao()
print(variavel)

################
print()
def funcao(var):
    print(var)
    
variavel = funcao('valor que eu quero') # printa na tela e retorna none
# pois nao defini nenhum return
#as linhas que defino após o return nao sera executada.

############
print()
def divisao(n1,n2):
    return n1/n2

divide = divisao(5,2)
print(divide)

############
print()
def divisao2(n1,n2):
    if n2>0:
        return n1/n2 #abaixo do return, nao executa outras instruções, exceto se eu colocar outra condição com return
        
resultado = divisao2(8,0) # divisao por zero
print(resultado) #neste caso retorna 'none'

if resultado:
    print(resultado)
else:
    print('Não é possivel fazer divisao por zero')

############
print()
def f(var):
    print(var)

def g():
    return f #Retorno a outra função

var = g() # a variavel vai receber a função f, pois g retorna f
print(type(var))
print(id(var),id(f))


