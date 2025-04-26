nums = []
for i in range(0, 10):
    num = int(input(f'Insira o {i+1}° número: '))
    nums.append(num)

pares = [str(n) for n in nums if n%2 == 0]
impares = [str(n) for n in nums if n%2 != 0]
listastr = [str(n) for n in nums]


print(f'Lista normal: {", ".join(listastr)}.')
print(f'Lista de pares: {", ".join(pares)}.')
print(f'Lista de impares: {", ".join(impares)}.')
