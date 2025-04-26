import time

num = int(input('Insira o começo da contagem regressiva: '))
n1 = num

for c in range(0,num+1):
    print(n1)
    n1 -= 1
    time.sleep(1)