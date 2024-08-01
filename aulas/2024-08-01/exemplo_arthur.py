import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = random.randint(0,10)


chute = int(input('Número: '))

posicoes = []
for i in range(10):
    if (chute == numeros[i]):
        posicoes.append(i)

if (len(posicoes) == 0):
    print('Não tem')
else:
    print('Tem:', posicoes)

print(numeros)
