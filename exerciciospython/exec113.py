def leia_int(inputf):
    while True:
        try:
            n = input(inputf)
            n = int(n)
        except:
            print('ERRO, por favor, digite um número inteiro válido!')
            continue
        else:
            return n


def leia_float(inputf):
    while True:
        try:
            n = input(inputf)
            n = float(n)
        except:
            print('ERRO, por favor, digite um número inteiro válido!')
            continue
        else:
            return  n


print(leia_int('Escreva um número Inteiro: '))
print(leia_float('Escreva um número Real: '))