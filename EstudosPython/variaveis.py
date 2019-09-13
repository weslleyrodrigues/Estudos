"""
Iniciar com letra, pode conter números, separar _ , letras minusculas
"""

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

#calcular indice de massa corporal
#altura x altura dividido pelo peso
imc = peso/(altura**2) #eleva ao quadrado

print(nome, 'tem', idade, 'anos de idade e seu IMC é: ', imc)