from random import randint as rd
jogos = []

qntd_jogos = int(input('Quantos jogos deseja fazer?\n'))

for i in range(qntd_jogos):
    jogo = []
    for i in range(6):
        jogo.append(f'{rd(0, 60):02}')
    jogos.append(jogo[:])

print('Os jogos gerados foram: ')
for jogo in jogos:
    print('(', end='')
    print(f'{"-".join(jogo)}', end='')
    print(')', end='')
    print()

