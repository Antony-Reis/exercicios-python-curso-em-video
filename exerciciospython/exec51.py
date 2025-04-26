p1 = int(input('Qual vai ser o primeiro termo da P.A.: '))

razao = int(input('Qual será a razão?: '))

for c in range(0, 10,):
    print(f'P{c+1} : {p1}')
    p1 += razao