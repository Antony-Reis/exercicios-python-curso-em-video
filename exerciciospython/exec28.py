import random

lista = [1,2,3,4,5]

numrandom = random.choice(lista)

num1 = input('O número foi escolhido pelo sistema\nQual número você acha que foi?\n')


if not num1.isnumeric():
   print('Coloque um número entre 1 e 5')
else:
    if int(num1) <= 1 or int(num1) >= 5:
        print('Coloque um número entre 1 e 5')
    else:
        if numrandom == int(num1):
            print(f'Você acertou\n{numrandom}={num1}')
        else:
            print(f'Errou feio\n{numrandom}!={num1}')


