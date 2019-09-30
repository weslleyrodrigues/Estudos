l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print(ex1)

print()
ex2 = [v*2 for v in l1]
print(ex2)

print()
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)

print()
l2 = ['Luiz','Mario','Maria']
ex4 = [v.replace('a','@')for v in l2] #alterando letras A por @
print(ex4)

