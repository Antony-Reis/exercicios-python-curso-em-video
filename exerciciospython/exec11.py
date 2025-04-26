lar = float(input('Insira a largura da parede: '))
com = float(input('Insira o comprimento da parede: '))
area = lar*com

tintane = area/2

print(f'Largura: {lar}M\nComprimento: {com}M\nÁrea: {round(area,2)}M²\nTinta necessária: {round(tintane,3)}L')
