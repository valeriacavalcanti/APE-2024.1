import random

numeros = list(range(1,20,2)) # gerar o vetor
random.shuffle(numeros) #embaralhar

menor = maior = numeros[0]
menor_i = maior_i = 0

for i in range(1,len(numeros)):
    if (numeros[i] > maior):
        maior = numeros[i]
        maior_i = i
        
    if (numeros[i] < menor):
        menor = numeros[i]
        menor_i = i

print(numeros)
print('menor:', menor, menor_i)
print('maior:', maior, maior_i)

