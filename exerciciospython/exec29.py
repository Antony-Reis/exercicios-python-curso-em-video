kmph = float(input('Quantos km/h ele passou?\n'))

if kmph<=80:
    print('De boa')
else:
    multa = round((kmph - 80) * 7, 2)
    print(f'O valo da multa será de R${multa}')