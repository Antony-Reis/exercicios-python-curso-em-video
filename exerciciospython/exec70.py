produto = []
valor = []

while True:
    controle = input('Deseja cadastrar algum produto? (s/n)')

    if controle == 's':
        produto.append(input('Digite o nome do produto: '))
        valor.append(float(input('Digite o valor do produto: ')))

    elif controle == 'n':
        if len(produto) == 0 or len(valor) == 0:
            print('Nada foi cadastrado')
        else:
            total = str(round(sum(valor), 2)).replace('.', ',')
            produtomilmais = sum(1 for v in valor if v > 1000)
            produtomaisbarato = produto[valor.index(min(valor))]

            print(f'O total da compra será de {total}\nTem {produtomilmais} produto que custam mais de 1000 reais\nO produto mais barato é {produtomaisbarato}')
            break