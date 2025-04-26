grupo = []

while True:
    pessoa = []
    control = input('Deseja inserir uma pessoa? s/n\n').lower()

    if control == 's':
        nome = input('Insira o nome da pessoa: ').capitalize()
        pessoa.append(nome)

        peso = int(input('Insira o peso da pessoa: '))
        pessoa.append(peso)

        grupo.append(pessoa[:])

        print('Pessoa cadastrada')

    elif control == 'n':
        print(f'Tivemos {len(grupo)} pessoas cadastradas')

        maiorpeso = 0
        menorpeso = 1000

        for i in range(0,len(grupo)):
            if grupo[i][1] > maiorpeso:
                maiorpeso = grupo[i][1]

            if grupo[i][1] < menorpeso:
                menorpeso = grupo[i][1]


        pessoasmaiorpeso = [grupo[p][0] for p in range(0, len(grupo)) if grupo[p][1] == maiorpeso]
        pessoamenorpeso = [grupo[p][0] for p in range(0, len(grupo)) if grupo[p][1] == menorpeso]

        print(f'As pessoa mais pesadas tem {maiorpeso}Kg ,são: {" ,".join(pessoasmaiorpeso)}')
        print(f'As pessoa mais leves tem {menorpeso}Kg ,são: {" ,".join(pessoamenorpeso)}')

        conti = input('Deseja continuar? s/n\n').lower()
        if conti == 's':
            continue
        else:
            print('Programa encerrado')
            break


    elif len(pessoa) == 0:
        print('Você tem que cadastrar uma pessoa.')
        continue

    else:
        print('Invalido')
        continue



