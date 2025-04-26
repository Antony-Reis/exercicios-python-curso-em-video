num = input('Coloque um número entre 0 e 9999\n')
num1 = int(num)

if num1>=0 and num1<=9999:
    print(f'Unidade: {num[3]}\nDezena: {num[2]}0\nCentena: {num[1]}00\nMilhar {num[0]}000')

else:
    print('Coloca o número certo')