num = int(input('Insira o primeiro número: '))
lista = []
controle = 0
lista.append(num)

while True:
    num1 = 0
    num1 = num

    lista.append(num)
    listastr = []
    if controle == 7:

        for l in lista:
            listastr.append(str(l))

        print(f'{"→".join(listastr)}')
        break
    controle += 1