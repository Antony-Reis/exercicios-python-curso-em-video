valor = float(input('Qual o valor da compra?'))

while True:
    cond = input(
        'Qual será a condição de pagmento?\n' + 33 * '=' + '\nav = Á vista dinheiro/cheque\nac = Á vista no cartão\nc2 = 2x no cartão\nc3 = 3x ou mais no cartão\n' + 33 * '=' + '\n')

    if cond =='av':
        valor = valor-valor*0.10
        print(f'O valor a ser pago a ser pago será R${valor}.')
        break

    elif cond == 'ac':
        valor = valor-valor*0.05
        print(f'O valor a ser pago a ser pago será R${valor}.')
        break

    elif cond == 'c2':
        print(f'O valor a ser pago será R${valor}.')
        break

    elif cond == 'c3':
        valor = valor+valor*0.20
        print(f'O valor a ser pago será R${valor}.')
        break
    elif cond == 'exit':
        break

    else:
        print('Por favor, insira a condição de pagamento correta.')