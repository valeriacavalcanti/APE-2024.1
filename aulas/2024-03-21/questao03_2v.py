fat = 1
num = int(input('Valor de N: '))

for i in range(num, 0, -1):
    fat = fat * i


print(f"{num}! = {fat}")
