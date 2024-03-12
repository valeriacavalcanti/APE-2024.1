#dia, mes, ano = input('Informe a validade: ').split('/')

data = input('Informe a validade: ')

dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

# dia, mes, ano = int(dia), int(mes), int(ano)

print(dia, mes, ano)

if (ano > 2024):
    print('Compre!')
else:
    if (ano < 2024):
        print('Reclame! Venceu ano anterior.')
    else:
        # ano é 2024
        if (mes > 3):
            print('Compre!')
        else:
            if (mes < 3):
                print('Reclame! Venceu mês anterior')
            else:
                # mês é 03
                if (dia >= 7):
                    print('Compre!')
                else:
                    print('Reclame! Venceu dia anterior')














