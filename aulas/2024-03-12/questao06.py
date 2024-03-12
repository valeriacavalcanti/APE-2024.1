nome = input('Nome: ')
conceito = input('Conceito: ')

if (conceito == 'A'):
    print(nome, 'é fortemente recomendado')
else:
    # NAO e fortemente recomendado
    if (conceito == 'B') or (conceito == 'C'):
        print(nome, 'é recomendado')
    else:
        print(nome, 'não é recomendado')
