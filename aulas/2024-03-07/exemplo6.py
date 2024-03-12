nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
frequencia = int(input('Frequência: '))

media = (nota1 + nota2)/2

if (frequencia < 75):
    print('reprovou por falta')
else:
    if (media >= 70):
        print('passou por média')
    else:
        if (media >= 40):
            print('Final')
        else:
            print('reprovou por nota')
