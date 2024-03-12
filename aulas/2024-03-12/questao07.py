peso = float(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / (altura**2)

if (imc < 18.5):
    grau = 'Baixo peso'
else:
    # imc é maior ou igual a 18.5
    if (imc < 25):
        grau = 'Normal'
    else:
        # imc é maior ou igual a 25
        if (imc < 30):
            grau = 'Sobrepeso'
        else:
            # imc é maior ou igual 30
            grau = 'Obesidade'

print(grau)
