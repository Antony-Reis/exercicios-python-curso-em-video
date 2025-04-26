num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dizesseis', 'dizessete', 'dizoito', 'dezenove', 'vinte')
while True:
    try:
        numinput = int(input('Insira um número entre 0 e 20: '))
        extenso = num[numinput]


    except ValueError:
        print("Erro de valor\nInsira um número inteiro")
        continue
    except IndexError:
        print("Erro de valor\nInsira um valor entre 0 e 20")
        continue
        
    print(f'O número escolhido foi {extenso}.')
    break