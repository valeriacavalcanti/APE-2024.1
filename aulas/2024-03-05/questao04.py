km_antes = int(input("Hodômetro antes: "))
km_depois = int(input("Hodômetro depois: "))
qt_litros = float(input("Quantidade de litros gasto: "))
valor_litro = float(input("Valor do litro: "))
capacidade_tanque = int(input("Capacidade do tanque: "))

# calcular a km rodada
km_rodada = km_depois - km_antes

# Distância percorrida por litro de combustível
eficiencia = km_rodada/qt_litros

# Autonomia do veículo
autonomia = capacidade_tanque * eficiencia

# custo da viagem
custo_viagem = qt_litros * valor_litro

print(f"Quilometragem rodada: {km_rodada}")
print(f"Eficiência do veículo: {eficiencia}")
print(f"Autonomia do veículo: {autonomia}")
print(f"Custo da viagem: R$ {custo_viagem:.2f}")



