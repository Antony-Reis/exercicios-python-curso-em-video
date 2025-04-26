import random
qntd = 1
while True:
    numinput = int(input(f'{qntd}° tentativa\nInsira um número inteiro entre 0 e 10: '))

    numrandom = int(round(random.random()*10, 0))

    if numrandom == numinput:
        print(f'O número do computador foi {numrandom} e o seu foi {numinput}, acertou.'
              f'\nVocê precisou de {qntd} tentivas.')
        break

    else:
        print(f'O número do computador foi {numrandom} e o seu foi {numinput}, errou.')
        qntd += 1
        continue