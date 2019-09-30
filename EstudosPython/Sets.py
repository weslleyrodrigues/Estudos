"""
add (adiciona), update (atualiza), clear, discard
Union | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas nos sets da esqueda)
simmetric_difference ^  (Elementos que estão nos dois sets, mas não em ambos)

Sets (conjuntos) so supurtam elementos unicos - Não tem chave valor
"""

#Exemplo1
set1 = {1,2,3,4,5,6,7,9876} 
print(set1)
print(type(set1))

#Exemplo2
set2 = set()  #criar um set vazil
set2.update([1,2,3,4,5,6,7,8,9])
print(set2)

print()

# Unindo dois sets
print('## Unindo dois Sets')
union = set1 | set2
print(union)
# Intersecion, Pega apenas valores em comum nos dois Sets
print('## Intersecion')
Intersecion = set1 & set2
print(Intersecion)
# Diference, pega a diferença apenas do set da esquerda
print('## Diference')
diference = set1 - set2
print(diference) # no caso o valor 9876 é exibido pois o mesmo contem no set1 e nao contem no set 2
# simmetric_difference - Elementos que estão nos dois sets, mas não em ambos
print('## Simmetric_difference')
simmetric = set1 ^ set2
print(simmetric)




