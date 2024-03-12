nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))

media = (nota1 + nota2)/2

print(f"Média = {media:.2f}")

if (media >= 70):
    print('Aprovado')
else:
    if (media >= 40):
        print('Final')
    else:
        print('Reprovado')
