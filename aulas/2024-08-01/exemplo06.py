import random

numeros = [0] * 10

for i in range(10):
    numeros[i] = random.randint(0,10)


chute = int(input('Número: '))

if (chute in numeros):
    print('tem:', numeros.index(chute))
else:
    print('nao tem')
    
print(numeros)
