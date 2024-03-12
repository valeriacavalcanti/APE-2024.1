valor_vendido = float(input('Valor vendido: '))

comissao = valor_vendido * 0.05

if (comissao < 1412):
    salario = 1412
else:
    salario = comissao


print('Salário: R$ {:.2f}'.format(salario))
