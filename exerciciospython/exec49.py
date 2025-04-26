lista = []
um = 1
while True:
    num = input('A tabuada será de que número?\n')

    if num.isnumeric():

        for c in range(1, 10):
             r = c*int(num)
             lista.append(str(r))

        for lista in lista:
            print(f'_____________\n{num} X {um} = {lista}')
            um += 1
        print('_____________')
        break


    else:
        print('Inválido')
        continue