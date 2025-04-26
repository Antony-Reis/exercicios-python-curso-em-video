lista = []

while True:
    num = input('Insira um número para a média(exit para parar): ')

    if num == 'exit':

        listaord = sorted(lista)

        print(f'A média entre os número inseridos é {round(sum(lista)/len(lista),2)} o maior número entre eles é {listaord[-1]} e o menor é {listaord[0]}')

        stop = input('Deseja parar o programa?\n(sim/nao)\n').lower()
        parar = stop == 'sim'

        if parar:
            print('Programa encerrado')
            break

        elif not parar:
            continue

    if num.isnumeric():
        lista.append(int(num))