num = int(input('Insira um número inteiro: '))
bool = False

for c in range(2,num):
    if  num%c == 0:
        bool = True
        break
if bool:
    print('Não é um número primo!')
else:
    print('É um número primo!')

