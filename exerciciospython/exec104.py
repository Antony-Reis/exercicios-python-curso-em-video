def leiaInt(inputf):
    while True:
        i = input(inputf)
        if i.isnumeric():
            print('É um número')
            return int(i)
        else:
            print('Não é número')
            continue


num = leiaInt('Digite um numero: ')
print(num)