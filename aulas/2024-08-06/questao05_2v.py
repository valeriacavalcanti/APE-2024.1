import random

numeros = list(range(1,20,2)) # gerar o vetor
random.shuffle(numeros) #embaralhar

menor = maior = 0

for i in range(1,len(numeros)):
    if (numeros[i] > numeros[maior]):
        maior = i
        
    if (numeros[i] < numeros[menor]):
        menor = i

print(numeros)
print('menor:', menor, numeros[menor])
print('maior:', maior, numeros[maior])

