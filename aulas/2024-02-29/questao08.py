nome = input('Nome: ')
nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
nota3 = int(input('Nota 3: '))

media = (nota1 + nota2 + nota3) / 3

#print(nome, '. Média = ', media, sep='')
print(f"{nome}. Média = {media:.2f}")


#print(f"{media:.2f}")
