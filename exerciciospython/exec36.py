valorcasa = float(input('Qual será o valor da casa?\n'))

salario = float(input('Qual é o seu salário?\n'))

anospagar = float(input('Em quantos anos deseja pagar?\n'))

valorcasames = valorcasa/(anospagar*12)

if valorcasames >= salario* 0.30:
    print('O empréstimo foi negado')
else:
    print('O empréstimo foi aceito')