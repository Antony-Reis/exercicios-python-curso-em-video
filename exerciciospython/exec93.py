jogador = dict()

jogador['nome'] = input('Nome: ').title()

qntd = int(input('Quantidade de jogos: '))
jogador['gols'] = []
for i in range(qntd):
    jogador['gols'].append(int(input(f'Gols na {i+1}° partida: ')))

jogador['total'] = sum(jogador['gols'])
print('='*40)
for k,v in jogador.items():
    if type(v) == list:
        print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
        for i in range(len(jogador['gols'])):
            print(f'Na {i+1}° partida: {jogador['gols'][i]} gols')

    else:
        print(f'{k.capitalize()}: {v}')