lista = []

qntd = input('Quantos pesos deseja ordenar: ')

for c in range(0, int(qntd)):
    peso = float(input('Insira o peso: '))
    lista.append(peso)

lista.sort()

lista = [str(c).replace('.', ',') for c in lista]

print(f'O ordem dos pesos foi : {" - ".join(lista)}.')