idade = []
sexo = []

while True:
    controle = input('Deseja cadastrar alguém? (s/n)')

    if controle == 's':
        idade.append(int(input('Digite a idade: ')))
        sexo.append(input('Digite o sexo (M/F): ').lower())

    elif controle == 'n':
        if len(idade) == 0 or len(sexo) == 0:
            print('Nada foi cadastrado')

        else:
            pessoamaior = 0
            homens = 0
            mulhervinte = 0
            controle = 0

            pessoamaior = sum(1 for i in idade if i >= 18)
            homens = sum(1 for s in sexo if s == 'm')
            mulhervinte = sum(1 for i, s in zip(idade, sexo) if s == 'f' and i < 20)

            print(f'Pessoas com mais de 18: {pessoamaior}\nQuantidade de homens cadstrados: {homens}\nMulheres com menos de 20 anos: {mulhervinte}')
            break