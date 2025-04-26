texto = input('Insira um texto')
texto = texto.replace(' ', '').lower()

if len(texto)%2 == 0:

    txt1 = texto[0:(int(len(texto)/2))]

    txt2 = texto[int(len(texto)/2):int(len(texto))+1]

    txt2 = txt2[::-1]

    if txt1 == txt2:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
else:
    texto = texto.replace(texto[int(round(len(texto)/2, 2))],'')

    txt1 = texto[0:(int(len(texto)/2))]

    txt2 = texto[int(len(texto)/2):int(len(texto))+1]

    txt2 = txt2[::-1]

    if txt1 == txt2:
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')
