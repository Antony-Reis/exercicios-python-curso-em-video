num1 = int(input('Insira o primeiro número: '))

num2 = int(input('Insira o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que o número {num2}')
elif num1 < num2:
    print(f'O número {num2} é maior que o número {num1}')
else:
    print(f'O número {num1} é igual ao número {num2}')