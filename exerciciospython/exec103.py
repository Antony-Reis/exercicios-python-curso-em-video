from funcoes import escrever_linha
from funcoes import linhas
def ficha(nome='desconhecido', golsf='0'):
    print(escrever_linha(f'O jogador {nome} fez {golsf} gol(s) no campeonato.'))

while True:
    linhas()
    nome_jogador = input('Nome do jogador\n(exit para sair)\n: ').strip()
    if nome_jogador == 'exit':
        break
    gols = input('Qunatidade de gols: ')
    linhas()
    ficha(nome_jogador, gols)