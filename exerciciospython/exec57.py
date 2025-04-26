lista = []
while True:
    se =  input('Insira o sexo: ').upper()

    if se == 'M':
        lista.append(se)
        print('Adicionado a lista')
    elif se == 'F':
        lista.append(se)
        print('Adicionado a lista')

    elif se == 'EXIT':
        print(f'Os sexos adicionados foram: {", ".join(lista)}.')
        break

    else:
        print('Inválido')
        continue