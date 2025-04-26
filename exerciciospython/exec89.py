alunos = []
while True:
    control = input('Deseja cadastrar alguem? s/n - "Buscar" para buscar uma nota de algum aluno pelo nome\n').lower()
    aluno = []
    if control == 's':
        aluno.append(input('Insira o nome do aluno: ').lower())
        aluno.append(int(input('Insira a primeira nota do aluno: ')))
        aluno.append(int(input('Insira a segunda nota do aluno: ')))
        alunos.append(aluno[:])

    elif control == 'exit' or control == 'sair':
        print('Programa encerrado')
        break

    elif len(alunos) == 0:
        print('A lista está vazia')
        continue

    elif control == 'n':
        for aluno in alunos:
            print(f'Aluno: {aluno[0].title()} | 1° nota: {aluno[1]} | 2° nota: {aluno[2]} | Média das notas: {(aluno[1]+aluno[2])/2}')


    elif control == 'buscar':
        encontrado = False
        nome = input('Pesquise o nome completo do aluno: ')
        for aluno in alunos:
            if aluno[0] == nome:
                print(f'Aluno: {aluno[0].title()} | 1° nota: {aluno[1]} | 2° nota: {aluno[2]}')
                encontrado = True
                break

        if not encontrado:
            print('Aluno não foi encontrado')



    else:
        print('Inválido')
        continue