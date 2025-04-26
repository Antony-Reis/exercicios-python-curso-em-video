idade = int(input('Inira a sua idade: '))

frase = 'Segundo a Confederaçao Nacional de Natação sua categoria é '

if 9>=idade>0:
    print(f'{frase}MIRIM')
elif 14>=idade >9:
    print(f'{frase}INFANTIL')
elif 19>=idade>14:
    print(f'{frase}JUNIOR')
elif 20==idade:
    print(f'{frase}SÊNIOR')
elif 120>idade>20:
    print(f'{frase}MASTER')
else:
    print(f'Como você tem {idade} anos?')