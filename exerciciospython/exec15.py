dias = int(input('Quantos dias o carro foi usado?\n'))

kmrodados = input('Quantos Km foram rodados com o carro?\n')
kmrodados1 = float(kmrodados.replace(',','.'))

diasvalor = dias*60

kmvalor = round(kmrodados1*0.15,2)
kmvalor1 = str(kmvalor).replace('.',',')

valortotal = round(kmvalor+diasvalor,2)
valortotal1 = str(valortotal).replace('.,',',')

print(f'O valor referente aos {dias} dias alugados é de R${diasvalor} e dos {kmrodados}Km rodados é de R${kmvalor1}.\nO valor total será de R${valortotal1}')
