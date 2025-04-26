import datetime

maiores = 0
menores = 0
anoatual = datetime.datetime.now().year

qntd = input('Quantos idades deseja saber(insira o ano de nascimento): ')

for c in range(0, int(qntd)):
    ano = int(input('Insira o ano\n'))

    if anoatual-ano >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Nós temos {maiores} maiores de idade e {menores} menores de idade')