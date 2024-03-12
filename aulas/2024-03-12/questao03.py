num1 = int(input('Número 1:'))
num2 = int(input('Número 2:'))
num3 = int(input('Número 3:'))

if (num1 > num2) and (num1 > num3):
    maior = num1
else:
    # num1 NÃO é o maior
    if (num2 > num3):
        maior = num2
    else:
        maior = num3

print('Maior:', maior)
