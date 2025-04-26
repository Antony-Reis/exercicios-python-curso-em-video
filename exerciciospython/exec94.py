pessoas = []

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ').title()

    while True:
        pessoa['sexo'] = input('Sexo (M/F): ').upper()
        if 'M' == pessoa['sexo'] or 'F' == pessoa['sexo']:
            break
        print('Inválido')

    pessoa['idade'] =  int(input('Idade: '))

    pessoas.append(pessoa)

    while True:
        sair = input('Deseja cadastrar mais pessoas? (s/n): ').lower()
        if sair == 's' or sair == 'n':
            break
        print('Inválido')

    if sair == 's':
        continue
    if sair == 'n':
        print(f'Foram cadastradas {len(pessoas)} pessoas')
        media = sum(i['idade'] for i in pessoas)/len(pessoas)
        print(f'A média de idade das pessoas é {media:.2f}')

        todas_mulheres = list(i['nome'] for i in pessoas if i['sexo'] == 'F')
        print(f'Lista com as mulheres: {", ".join(todas_mulheres)}' if len(todas_mulheres) != 0 else 'Não tem nenhuma mulher na lista')

        todas_idade_acima_media = list(i['nome'] for i in pessoas if i['idade'] >= media)
        print(f'Pessoa(s) com idade acima da média: {", ".join(todas_idade_acima_media)}.' if len(todas_idade_acima_media) != 0 else 'Não tem pessoas com idade acima da média')
        break