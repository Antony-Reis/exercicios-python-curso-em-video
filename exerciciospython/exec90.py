dc = {}

dc['Nome'] = input('Insira o nome: ').title()

dc['Media'] = float(input(f'Insira a média de {dc['Nome']}: '))



print(f'O nome é igual a {dc['Nome']}')
print(f'A média é igual a {dc['Media']}')
print('Foi aprovado' if dc['Media'] >= 7 else 'Não foi aprovado')