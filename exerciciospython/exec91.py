from random import randint as rd
from time import sleep as sp
from operator import itemgetter
jogos = {'jogador1':rd(1, 6),'jogador2':rd(1, 6),'jogador3':rd(1, 6),'jogador4':rd(1, 6)}
for k,v in jogos.items():
    print(f'O {k} tirou o número {v}')
    sp(1)

jogosord = dict(sorted(jogos.items(), key=itemgetter(1), reverse=True))
contador = 1
for k,v in jogosord.items():
    print(f'{contador}° lugar: {k} com {v}')
    contador += 1
    sp(1)