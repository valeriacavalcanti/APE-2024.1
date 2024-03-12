nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
frequencia = int(input('Frequência: '))

media = (nota1 + nota2)/2

if (media >= 70) and (frequencia >= 75):
    print('aprovado')
else:
    print('não aprovado')
