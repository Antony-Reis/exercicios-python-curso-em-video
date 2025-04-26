time=('Corinthians', 'Ceará', 'BotaFogo', 'Bahia', 'Atlético Mineiro', 'Cruzeiro', 'Flamengo', 'Fluminence', 'Fortaleza', 'Palmeira', 'Mira Sol', 'Juventude', 'Internacional', 'Grêmio', 'Vitória', 'Vasco Da Gama', 'Esporte', 'São Paulo', 'Santos', 'Bragantino')




timesalfa = sorted(time)


print(f'Os 5 primeiros são : {", ".join(time[0:5])}.')
print(f'Os 4 ultimos são: {", ".join(time[-4:])}')
print(timesalfa)

try:
    posiccruzeiro = time.index('Cruzeiro') + 1
    print(f'O cruzeiro se encontra em {posiccruzeiro}° lugar.')
except ValueError:
    print('O cruzeiro não se encontra na lista.')

