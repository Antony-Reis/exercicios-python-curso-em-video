from datetime import datetime
anoatual = datetime.now().year
print('='*36+'\nVerifique se você precisa se alistar\n'+'='*36)
anonas = int(input('Insira o seu ano de nascimento: '))

idade = anoatual - anonas

if 17 > idade > 0:
    print(f'Você tem {idade}, só irá se alistar daqui a {17-idade} ano(s).')

elif idade == 17 or idade ==18:
    print(f'Você tem {idade}, está na hora de se alistar.')

elif 18 < idade < 100:
    print(f'Você tem {idade}, seu alistamento esta atrasado em {idade-18} anos(s).')

else:
    print(f'Como você tem {idade} anos?')