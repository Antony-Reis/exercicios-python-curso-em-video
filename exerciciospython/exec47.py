inicio =  int(input('Insira o inicio da contagem de pares: '))

fim =  int(input('Insira o inicio da contagem de pares: '))
pares = []

for c in range(inicio, fim+1):
    if c%2 == 0:
        pares.append(str(c))

print(f'Os números pares entre {inicio} e {fim} são: {", ".join(pares)}')