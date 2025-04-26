from random import choice as ch
from random import randint as rd
from funcoes import linhas


def sorteia_soma(*num):
    l = list()
    num = num[0]
    for i in range(5):
        n = ch(num)

        while n in l:
            n = ch(num)
        l.append(n)
    s = sum(n for n in l if n % 2 == 0)
    return l, s


lista = list()
while True:
    try:
        fim = int(input('Insira quantos números deexseja ter na lista(mais de 5): '))
        if fim <= 5:
            print('Inválido - Insira um número maior que 5')
            continue
        else:
            break
    except ValueError:
        print('Inválido - Insira um número inteiro')

for i in range (0, fim):
    lista.append(rd(0, 100))

lista_sorteada, soma_pares_lista_sorteada = sorteia_soma(lista)

linhas()
print(f'Lista: {lista}')
linhas()
print(f'Lista sorteada: {lista_sorteada}')
linhas()
print(f'A soma de todos os pares da lista sorteada é: {soma_pares_lista_sorteada}')
linhas()