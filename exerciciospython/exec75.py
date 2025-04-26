num = (int(input('Insira um valor inteiro: ')), int(input('Insira um valor inteiro: ')), int(input('Insira um valor inteiro: ')), int(input('Insira um valor inteiro: ')))
pares = []
qntdnove = num.count(9)

for n in num:
    if n%2 == 0:
        pares.append(str(n))

print(f'Os números foram: {num}\nO número 9 apareceu {qntdnove} vezes')

try:
    indextres = num.index(3)
    print(f'O primeiro 3 está na {indextres+1}° posição')

except ValueError:
    print('Não há 3 na tupla')

if len(pares) != 0:

    print(f'Os número pares digitados foram: {", ".join(pares)}.')
else:
    print('Nenhum número par foi digitado')