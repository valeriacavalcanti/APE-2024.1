num = int(input('Valor: '))
maior = num
menor = num

for i in range(3):
    num = int(input('Valor: '))
    if (num > maior):
        maior = num
    else:
        if (num < menor):
            menor = num


print('Menor:', menor)
print('Maior:', maior)

