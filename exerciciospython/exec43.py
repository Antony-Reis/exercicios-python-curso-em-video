peso = float(input('Isnira o seu peso: '))

altura = float(input('Insira sua altura: '))

imc = round(peso/altura**2, 2)

if imc<18.5:
    print(f'O seu IMC é {imc}. Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'O seu IMC é {imc}. Peso ideal')
elif 25<= imc <30:
    print(f'O seu IMC é {imc}. Sobrepeso')
elif 30<= imc <40:
    print(f'O seu IMC é {imc}. Obesidade')
elif 40 <= imc:
    print(f'O seu IMC é {imc}. Obesidade mórbida')