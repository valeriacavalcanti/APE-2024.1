qt = 0
qt_acima_media = 0
soma = 0
numeros = [0,0,0,0,0,0]

for i in range(6):
    numeros[i] = int(input('Número: '))
    soma += numeros[i] # soma = soma + numeros[i]
    if (numeros[i] > 20):
        qt += 1 # qt = qt + 1


# foooora do for
media = soma/(i + 1)

for i in range(6):
    if (numeros[i] > media):
        qt_acima_media += 1 # qt_acima_media = qt_acima_media + 1

print('Soma:', soma)
print('Quantidade acima de 20:', qt)
print(f'Média: {media:.2f}')
print('Quantidade acima da média:', qt_acima_media)
