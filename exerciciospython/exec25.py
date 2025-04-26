nome = input('Insira o nome completo :')
nome1 = nome.title().strip()

if'Silva' in nome1:
    print(f'{nome1} tem Silva no nome')
else:
    print(f'Não há Silva em {nome1}')