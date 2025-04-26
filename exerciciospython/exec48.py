inicio =  input('Insira o inicio da soma dos impares múltiplos de 3: ')

fim =  input('Insira o inicio da impares múltiplos de 3: ')

lista = []
contagem = 0

for c in range(int(inicio), int(fim)+1):

    if not c%2 == 0:

        if c%3 == 0:
            contagem += 1
            lista.append(str(c))

if len(lista) == 0:
    print('Não há nenhum número que atenda as condições')

else:
    print(f'Há {contagem} número(s) impares múltiplos de 3 que estão entre  {inicio} e {fim} : {", ".join(lista)}.')