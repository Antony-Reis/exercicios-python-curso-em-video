import random
escolhahumana = numhumano = numpc = 0

while True:
    numpc = random.randint(1, 10)
    escolhahumana = input('Escolha se será impar ou par: ').lower()
    numhumano = int(input('Escolha um número entre 1 e 10: '))

    if escolhahumana == 'par':
        print('Você escolheu par e o PC ficou com impar')
        soma = numpc + numhumano

        if soma%2 == 0:
            print(f'Você Ganhou\nVocê escolheu {numhumano} e o PC escolheu {numpc}, ocasionando {soma}')
            continue
        else:
            print(f'Você perdeu\nVocê escolheu {numhumano} e o PC escolheu {numpc}, ocasionando {soma}')
            print('Programa encerrado')
            break

    if escolhahumana == 'impar':
        print('Você escolheu impar e o PC ficou com par')
        soma = numpc + numhumano

        if soma % 2 != 0:
            print(f'Você Ganhou\nVocê escolheu {numhumano} e o PC escolheu {numpc}, ocasionando {soma}')
            continue
        else:
            print(f'Você perdeu\nVocê escolheu {numhumano} e o PC escolheu {numpc}, ocasionando {soma}')
            print('Programa encerrado')
            break