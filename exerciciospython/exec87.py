matriz = []
linhas = int(input('Quantidade de linhas da matriz: '))
colunas = int(input('Qunatidade de colunas da matriz: '))


for l in range (0, linhas):
    linha = []

    for c in range(0 ,colunas):

        num = int(input(f'Insira algum valor: {c+1}° coluna - {l+1}° linha: '))
        linha.append(num)


    matriz.append(linha[:])

for m in matriz:
    print(m)

somapares = 0
soma_terceira_linhas = 0

for l in range(0, linhas):
    for c in range(0, colunas):
        if matriz[l][c]%2 == 0:
            somapares += matriz[l][c]

        if c == 2:
            soma_terceira_linhas += matriz[l][c]

maiorvalorsegundalinha = max(matriz[1])

print(f'A soma de todos os valores pares é {somapares}\nA soma de todos os números da terceira coluna é {soma_terceira_linhas}\nO maior valor da segunda linha é {maiorvalorsegundalinha}')