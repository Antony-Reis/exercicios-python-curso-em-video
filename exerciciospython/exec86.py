matriz = []
linhas = int(input('Quantidade de linhas da matriz: '))
colunas = int(input('Qunatidade de colunas da matriz: '))

for i in range (0, linhas):
    linha = []

    for j in range(0 ,colunas):

        num = int(input(f'Insira algum valor: {j+1}° coluna - {i+1}° linha: '))
        linha.append(num)

    matriz.append(linha[:])

for m in matriz:
    print(m)
