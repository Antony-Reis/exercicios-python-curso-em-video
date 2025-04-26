lista = []
for i in range(7):
    num = int(input(f'Insira o {i+1}° número inteiro: '))
    if num %2 == 0:
        lista.insert(0,num)
    else:
        lista.append(num)

pares = [p for p in lista if p%2 == 0]
impares = [i for i in lista if i%2 != 0]
pares.sort()
impares.sort()

print(pares)
print(impares)