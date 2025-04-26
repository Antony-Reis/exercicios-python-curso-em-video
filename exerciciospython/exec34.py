salaori = float(input('Insira o sálario: '))

if salaori >= 1250.00:
    print(f'R${salaori}\nR${salaori+salaori*0.10}')
else:
    print(f'R${salaori}\nR${salaori + salaori * 0.15}')