from math import sqrt
catop = float(input('Coloque o valor do seu cateto oposto: '))
catad = float(input('Coloque o valor do seu cateto adjacente: '))

hipotenusa = sqrt(catop**2+catad**2)
print(f'O valor da hipotenusa é de {hipotenusa}')