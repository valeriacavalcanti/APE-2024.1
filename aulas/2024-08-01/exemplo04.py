import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = random.randint(0,10)


chute = int(input('Número: '))

existe = False
for i in range(10):
    if (chute == numeros[i]):
        existe = True
        break

if (existe == True):
    print('Tem')
else:
    print('Não tem')

print(numeros)
