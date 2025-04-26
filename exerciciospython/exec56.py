class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

lista = []
qntd = int(input('Quantos pessoas deseja inserir: '))

for c in range(0, qntd):
    nome = input(f'Pessoa {c + 1} - Qual seu nome? ')
    idade = int(input('Qual a sua idade? '))
    sexo = input('Qual o seu sexo (M/F)? ').strip().upper()
    lista.append(Pessoa(nome, idade, sexo))

media_idade = sum(p.idade for p in lista) / qntd

# Encontrar o homem mais velho
homens = [p for p in lista if p.sexo == 'M']
homem_mais_velho = max(homens, key=lambda p: p.idade, default=None)

# Contar mulheres com menos de 20 anos
mulheres_menos_20 = sum(1 for p in lista if p.sexo == 'F' and p.idade < 20)

# Exibir os resultados
print(f'\nA média de idade do grupo é {media_idade:.2f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho é {homem_mais_velho.nome}, com {homem_mais_velho.idade} anos.')
else:
    print('Não há homens no grupo.')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}')