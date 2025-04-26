numsdis = []
qntd = int(input('Quantos números deseja adicionar: '))
control = 1
while True:
    num = int(input(f'Insira o {control}° valor: '))

    if len(numsdis) == 0:
        numsdis.append(num)
        control += 1
    else:
        if num in numsdis:
            print('Valor repetido\nInsira outro')
            continue
        else:
            numsdis.append(num)
            if control == qntd:
                print(numsdis)
                break

        control += 1