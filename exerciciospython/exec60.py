num = int(input('Insira o número: '))
lista = []
numcontrole = 1

while True:
    valorfa = 1

    if numcontrole > num:
        for l in lista:
            valorfa *= l

        lista.sort(reverse=True)
        listastr = []

        for l in lista:
            listastr.append(str(l))

        print(f'{num}! = {"x".join(listastr)} = {valorfa}')
        break
    lista.append(numcontrole)
    numcontrole += 1