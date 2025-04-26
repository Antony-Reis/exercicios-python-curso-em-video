tamanho = float(input('Qual será a distancia da viagem?\n'))

if tamanho <= 200:
    print(f'O valor será de R${0.50*tamanho}')
else:
    print(f'O valor será de R${0.45*tamanho}')
