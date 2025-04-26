lista = []
lista.append(float(input('Insira um lado de triângulo: ')))
lista.append(float(input('Insira um lado de triângulo: ')))
lista.append(float(input('Insira um lado de triângulo: ')))

lista.sort()

if lista[0] + lista[len(lista)//2]  >  lista[len(lista)-1]:

    if len(lista) == len(set(lista)):
        print('Eles podem formar um triângulo escaleno')

    elif len(set(lista)) == 2:
        print('Eles podem formar um triângulo isósceles')

    elif len(set(lista)) == 1:
        print('Eles podem formar um triângulo equilátero')

else:
    print('Eles não podem formar um triângulo')