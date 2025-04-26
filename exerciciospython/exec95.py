jogadores = list()
while True:
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
    print('=' * 40)
    jogadores.append(jogador)

    while True:
        controle = input('Deseja inserir outro jogador ou buscar um jogador? (s/n/buscar)\n').lower()

        if controle == 'buscar':
            nome_jogador = input('Digite o nome do jogador: ').title()
            print('=' * 40)
            encontrado = True
            for j in jogadores:
                if j['nome'] == nome_jogador:
                    print('Levantamento do jogador')
                    print(f'O jogador {j['nome']} jogou {len(j['gols'])} partidas.')
                    encontrado = False
                    for i in range(len(j['gols'])):
                        print(f'Na {i + 1}° partida: {j['gols'][i]} gols')
                elif encontrado:
                    print('Jogador não consta')
            print('=' * 40)
            continue

        if controle == 's' or controle == 'n':
            break

        print('Inválido')
    if controle == 's':
        continue

    elif controle == 'n':
        for j in jogadores:
            print('=' * 40)
            print(f'O jogador {j['nome']} jogou {len(j['gols'])} partidas.')
            for i in range(len(j['gols'])):
                print(f'Na {i + 1}° partida: {j['gols'][i]} gols')
            print('=' * 40)
        break