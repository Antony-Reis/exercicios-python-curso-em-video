def maior(* num):
    m = max(num)
    l = list(num)
    return m, l


from random import random as rd
while True:
    sair = input('sair? s/n')
    if sair=='s':
        print('Programa encerrado')
        break
    else:
        maiorn, lista = maior(rd(), rd(), rd(), rd(), rd())
        print(lista)
        print(maiorn)