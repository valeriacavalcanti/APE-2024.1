import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = random.randint(0,10)


chute = int(input('Número: '))

posicao = -1
for i in range(10):
    if (chute == numeros[i]):
        posicao = i
        break

if (posicao == -1):
    print('Não tem')
else:
    print('Tem:', posicao)

print(numeros)
