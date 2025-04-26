ano = int(input('Insira um ano: '))
anoresto = ano%4
if anoresto == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')