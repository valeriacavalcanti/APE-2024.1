qtd = int(input('Quantidade de pessoas: '))
#qtd_m = qtd_f = 0
qtd_m = 0
qtd_f = 0

for i in range(qtd):
    sexo = input('F ou M? ')
    if (sexo == 'F'):
        qtd_f = qtd_f + 1
    else:
        qtd_m = qtd_m + 1

p_f = (qtd_f/qtd) * 100
p_m = (qtd_m/qtd) * 100

print(p_f)
print(p_m)
