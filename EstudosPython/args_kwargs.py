"""
Eles não precisam necessariamente se chamarem args, mas necessitam do asterisco
 O nome “args” é uma convenção.
 
"""

def func(*args):
    for arg in args:
        print(arg)
func(1,2,3,4,5,6)
print()

l = [1,2,3,44,55,'ola','hello']
func(*l)

#Valores Dafault
print()
def Func2(x=200,y=400):
    print ('{} {}'.format(x,y))
Func2()
#alterando os valores default
Func2(x=900,y=700)

#Kwargs - argumentos nomeados
def Func3(**kwargs):
    for item in kwargs.items():
        print (item)
Func3(x=300,f=988)

