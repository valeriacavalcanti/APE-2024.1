import random

n = int(input('N: '))
numeros = [0] * n
indices = []

for i in range(len(numeros)):
    numeros[i] = random.randint(1,8)
    #numeros[i] = int(input('Valor: '))

k = int(input('Chute: '))

# procurar o valor k no vetor "numeros"
for i in range(n):
    if (numeros[i] == k):
        indices.append(i)

# verificar se tem ou nao
if (len(indices) > 0):
    print('Achei:', indices)
else:
    print('Não achei')
