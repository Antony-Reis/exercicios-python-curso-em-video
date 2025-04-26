p1 = int(input('Qual vai ser o primeiro termo da P.A.: '))
razao = int(input('Qual será a razão?: '))
termos = int(input('Quantos termos será?: '))

n = 0

while True:

    while n < termos:
        print(f'P{n + 1} : {p1}')
        p1 += razao
        n += 1

    controle = input('Deseja mostrar mais quantos termos?\n')

    if controle.isnumeric():
        termos = int(controle)+n
        continue
    else:
        break
