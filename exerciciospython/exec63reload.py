import time


size = int(input('Insira a quantidade de termos da Sequência de Fibonacci deseja: '))

inicio = time.time()

lista = []

print('1→', end='')
if size > 2:
    lista.append(1)
    while True:
        num1 = lista[len(lista)-1] + lista[len(lista)-2]
        lista.append(num1)

        if size == 0:

            listastr = [str(l) for l in lista]


            print(f'{"→".join(listastr)}')

            break
        size -= 1

fim = time.time()
print(fim - inicio)