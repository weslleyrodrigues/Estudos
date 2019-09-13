#F- Strings 

nome = 'Weslley Rodrigues'
idade = 21 #int
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 60

print ('Nome: ', nome)
print ('Idade: ', idade)
print ('Altura: ', altura)
print ('É maior: ', e_maior)
print ('Peso: ', peso)

print (idade * altura)
imc = peso/(altura**2) #eleva ao quadrado

print(nome, 'tem', idade, 'anos de idade e seu IMC é: ', imc)

# Segunda forma de exibir valores 
print (f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}') #  :.2f estou arredondando o vador para 2 casas decimais após a virgula

# Terceira forma de exibir valores
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome,idade,imc))
#   :.2f estou arredondando o vador para 2 casas decimais após a virgula

# Caso eu queira exibir em outra ordem
#enumero as posições
print('{0} tem {2} anos de idade e seu IMC é {1}'.format(nome,idade,imc))

# utilizar parametros nomeados
#utilizo as siglas inves dos numeros
print('{n} tem {i} anos de idade e seu IMC é {im}'.format(n=nome, i=idade, im=imc))
