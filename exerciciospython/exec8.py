print('Conversor de metros\npe = Pés / po = Polegadas / mi = Milhas')
selec = input('Selecione a unidade que deseja converter\n')

n = float(input('Insira '))

if (selec == 'pe'):
        n1 = n * 3.28084
        print(f'{n} metros são {n1} pés')
if (selec == 'po'):
        n2 = n * 39.37008
        print(f'{n} metros são {n2} polegadas')
if (selec == 'mi'):
        n3 = n * 0.0006
        print(f'{n} metros são {n3} milhas')



