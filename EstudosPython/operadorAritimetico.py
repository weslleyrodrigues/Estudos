"""
+ 
-
*
/
// a divisao é aredondada
** potenciação
% móduto - resto da divisao
() alternar a precedencia das contas
"""
print('multiplicação: ',10*10)
print('Adição: ', 10+10)
print('subtração: ', 10-5)
print('divisao: ', 10/2)

print(10*'10') #exibe dez vezes o numero dez
print('5'+'5') # faz concatenação

#Obs, nao posso concaternar string com inteiro
#print('Weslley'+''+'Rodrigues tem '+ 21 + 'anos')

#forma correta:
print('Weslley'+''+'Rodrigues tem '+ '21' + 'anos')
#ou
print('Weslley'+''+'Rodrigues tem '+ str(21) + 'anos')

print(10//3) #arredonda o valor

print(2**10) #potenciação

print(10%3) #resto da divisao

print(5+2*10)
print((5+2)*10)


