from exerciciospython.funcoes import escrever_linha

def leia_int(inputf):
    while True:
        try:
            n = input(inputf)
            n = int(n)
        except:
            print('ERRO, por favor, digite um número inteiro válido!')
            continue
        else:
            return n

def mostrar_pessoas():
    with open('pessoa_cadastradas.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def cadastrar_pessoa(nome, idade):
    with open('pessoa_cadastradas.txt', 'a') as arquivo:
        arquivo.write(f'\n{str(nome).upper().ljust(35)}{str(idade).rjust(3)} ANOS')

while True:

    print(escrever_linha('menu principal'))

    try:
        while True:
            escolha = int(input('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do programa\n'))
            if 1 > escolha or escolha > 3:
                print('ERRO, Escolha uma das opções!')
                continue
            else:
                break

    except (ValueError, TypeError): print('ERRO, Escolha uma das opções!')

    if escolha == 3:
        print('Programa encerrado')
        break

    elif escolha == 1:
        mostrar_pessoas()
        print('='*44)

    elif escolha == 2:
        cadastrar_pessoa(input('Insira o nome completo da pessoa: '), leia_int('Insira a idade da pessoa: '))