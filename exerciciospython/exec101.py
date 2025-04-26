from datetime import datetime
from funcoes import escrever_linha
def voto(ano_nascimento):
    ano_atual = int(datetime.now().strftime("%Y"))

    idade = ano_atual - ano_nascimento

    if 16 > idade > -1:
        return "NEGADO", idade
    elif idade == 16 or idade == 17:
        return "OPCIONAL", idade
    elif 18 <= idade <= 120:
        return "OBRIGATÓRIO", idade
    else:
        return "Valor inválido", 0

while True:
    try:
        ano_nascimentov = int(input('Insira o ano de nascimento\n999 para sair\n'))
        if ano_nascimentov == 999:
            print('Programa encerrado')
            break
    except ValueError:
        print(escrever_linha('Erro\nInsira um ano inteiro!'))
        continue

    situacao, idadev = voto(ano_nascimentov)

    print(escrever_linha(f'Como você tem {idadev} anos o seu voto é: {situacao}') if situacao != 'Valor inválido' else escrever_linha('Idade inválida'))
