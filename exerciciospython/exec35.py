lista = []
lista.append(int(input('Insira um lado de triângulo: ')))
lista.append(int(input('Insira um lado de triângulo: ')))
lista.append(int(input('Insira um lado de triângulo: ')))

lista.sort()

if lista[0] + lista[len(lista)//2]  >  lista[len(lista)-1]:
    print('Eles podem formar um triângulo')
else:
    print('Eles não podem formar um triângulo')


