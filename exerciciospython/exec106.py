from funcoes import escrever_linha

while True:
    print(escrever_linha('SISTEMA DE AJUDA PyHELP'))
    funbi = input('Função ou biblioteca: ')
    if funbi == 'sair':
        print('Programa encerrado: ')
        break
    print(escrever_linha(f'acessando o manual do comando ({funbi})'))
    help(funbi)