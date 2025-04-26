from datetime import datetime

anoatual = int(datetime.now().strftime('%Y'))
pessoas = dict()

pessoas['nome'] = input('Nome: ').title()

pessoas['idade'] = anoatual - int(input('Ano de nascimento: '))
pessoas['ctps'] = int(input('Número da CTPS (0 não tem): '))

if pessoas['ctps'] != 0:
    pessoas['idadeaposentadoria']= 65 - (anoatual - (int(input('Ano da contratação: '))))
    pessoas['salario'] = float(input('Sálario: '))

for k,v in pessoas.items():
    if k == 'ctps':
        break
    print(f'{k.capitalize()}: {v}')

