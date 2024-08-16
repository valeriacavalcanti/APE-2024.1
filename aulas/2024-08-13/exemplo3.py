"""
Programa para declarar uma matriz
com tamanho 3x4.
Armazenar valores aleatórios
(entre 0 e 20)
"""

import random

# declarar matriz
matriz = []
for i in range(3):
    matriz.append([0] * 4)

# preencher com valores aleatórios
for i in range(3):
    for j in range(4):
        #print(i, j)
        matriz[i][j] = random.randint(0,20)

# imprimir a matriz (por linha)
for i in range(3):
    print(i, matriz[i])

# imprimir a matriz (por elemento)
for i in range(3):
    for j in range(4):
        print(i, j, matriz[i][j])

# imprimir a matriz toda
print(matriz)
