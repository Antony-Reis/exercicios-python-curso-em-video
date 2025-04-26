lista = []
lista2 = []

qntd = input('Quantos números deseja somar(só os pares): ')

for c in range (0, int(qntd)):
    num = input(f'Insira o {c+1}° número: ')
    if int(num)%2 == 0:
        lista.append(int(num))
        lista2.append(str(num))

print(f'A soma dos números {", ".join(lista2)} pares será {sum(lista)}')