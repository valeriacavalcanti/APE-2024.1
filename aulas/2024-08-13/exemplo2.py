matriz = []
for i in range(10):
    matriz.append([0]*10)

#print(matriz)
print(len(matriz))

# alterar os elementos da
# primeira linha para
# valor 10

for i in range(10):
    matriz[1][i] = 10


# alterar os elementos da
# segunda linha para
# valor -1

for i in range(10):
    matriz[2][i] = -1

# alterar todos os
# valores para -1
for i in range(10):
    for j in range(10):
        matriz[i][j] = -1
        


# exibir a matriz
for i in range(10):
    print(i, matriz[i])
