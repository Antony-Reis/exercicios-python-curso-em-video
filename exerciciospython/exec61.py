p1 = int(input('Qual vai ser o primeiro termo da P.A.: '))
n = 0
razao = int(input('Qual será a razão?: '))

while n < 10:
    print(f'P{n + 1} : {p1}')
    p1 += razao
    n += 1