num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

while True:
    controle = str(input('='*100+'\n'+f'1° número: {num1}\n2° número: {num2}\nO que deseja fazer?\n[1] somar - [2] multiplicar - [3] maior - [4] novos números - [5] sair do programa\n'+'='*100+'\n'))

    if controle == '1':
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é {soma}')

    elif controle == '2':
        multi = num1 * num2
        print(f'A multiplação de {num1} e {num2} é {multi}')

    elif controle == '3':
        if num1 > num2:
            print(f'{num1} é maior do que {num2}')
        elif num1 < num2:
            print(f'{num2} é maior do que {num1}')
        elif num1 == num2:
            print(f'{num1} é igual a {num2}')

    elif controle == '4':
        print('Insira os novos números')
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))

    elif controle == '5':
        print('Programa encerrado')
        break

    else:
        print('Inválido')
        continue