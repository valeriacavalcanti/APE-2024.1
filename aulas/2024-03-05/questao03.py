num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

aux = num1
num1 = num2
num2 = aux

print(num1, num2)

# solução python
num1, num2 = num2, num1
print(num1, num2)
