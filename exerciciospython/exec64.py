lista = []
while True:
    num = float(input('Insira um número para a soma (999 para parar a soma): '))

    if num == 999:
        print(f'Foram digitados {len(lista)} números e a soma entre eles é de {sum(lista)}')
        break

    lista.append(num)