print('='*31+'\nVerificar se você foi aprovado\n'+'='*31)

qntd = int(input('Quantidade de notas que deseja somar: '))

notas = []
n = 1

while qntd >= n:
    nota = float(input(f'Insira a {n}° nota: '))
    notas.append(nota)
    n = n+1

media = sum(notas) / qntd

if 10 >= media >= 7:
    print(f'A sua média foi de {media}, você foi aprovado 😁😁')
elif  7 > media >=5:
    print(f'A sua média foi de {media}, direto para a recuperação😒')
elif 5 > media >= 0:
    print(f'A sua média foi de {media}, Você foi reprovado😢🤦‍♂️')
else:
    print(f'A sua média deu {media}, como você conseguiu fazer isso')
