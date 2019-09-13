"""
Com o *args, consigo passa varios (ou apenas 1) parametros, e mesmo que eu nao passe nada
os mesmos podem ser rodado sem erros.
"""
def titulos_copa_do_mundo(pais,*args): 
    print ('País: ',pais)
    for titulo in args:
        print('Ano: ',titulo)
titulos_copa_do_mundo('Brasil',1958,1962,1970,1994,2002)
print()
titulos_copa_do_mundo('Afeganistão')
print ()
"""
Com o **kwargs eu utilizo os parametros nomeados. e mesmo que eu nao passe nada
os mesmos podem ser rodado sem erros.
"""
def calculo_de_preco(valor,**kwargs):
    taxa_porcentagem = kwargs.get('taxa_porcentagem')
    desconto = kwargs.get('desconto')
    
    if taxa_porcentagem:
        valor += valor * (taxa_porcentagem/100)
    if desconto:
        valor -= desconto
    return valor
    
#Passando um valor sem nenhum desconto    
preco_final = calculo_de_preco(100)
print(preco_final)
#Passando um valor com um desconto de 50%
preco_final = calculo_de_preco(100,desconto=50)
print(preco_final)
#Adicionando uma taxa
preco_final = calculo_de_preco(100,taxa_porcentagem=5)
print(preco_final)
