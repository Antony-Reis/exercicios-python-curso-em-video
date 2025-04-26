def leia_dinheiro(inputf):
    while True:
        num = input(inputf)

        if num.isnumeric():
            return float(num)
        else:
            print('Valor inválido')