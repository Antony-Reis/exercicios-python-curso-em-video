lista = []
for l in range(0,5):
    num = int(input('Insira um número: '))

    if len(lista)==0 or num > lista[-1]:
        lista.append(num)

    else:
        i = 0
        while i < len(lista):

            if num <= lista[i]:

                lista.insert(i, num)
                break

        i += 1





print(lista)