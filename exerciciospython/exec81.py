lista = []
for i in range(0, 7):
    num = int(input(f'Insira o {i+1}° número: '))
    lista.append(num)


print(f'A lista {lista}\nTem {len(lista)} números nela\nDecrescente: {sorted(lista, reverse=True)}')
print('Tem o valor 5 na lista' if 5 in lista else 'Não tem o valor 5 na lista')

