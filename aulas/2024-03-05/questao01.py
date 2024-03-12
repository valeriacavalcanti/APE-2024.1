nome = input('Informe o nome: ')
qt_carros = int(input('Quantidade carros: '))
valor_vendas = float(input('Valor das vendas: '))

salario = 1000 + (qt_carros*200) + (valor_vendas*0.05)

print(f"Salário = R$ {salario:.2f}")
print("Salário = R$ {:.2f}".format(salario))
