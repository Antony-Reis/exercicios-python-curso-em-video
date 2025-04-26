valorsacar = int(input('Qual valor será sacado? '))
notas50 = notas20 = notas10 = notas1 = 0

while valorsacar - 50 >= 0:
    notas50 +=1
    valorsacar -= 50

while valorsacar - 20 >= 0:
    notas20 +=1
    valorsacar -= 20

while valorsacar - 10 >= 0:
    notas10 +=1
    valorsacar -= 10

while valorsacar - 1 >= 0:
    notas1 +=1
    valorsacar -= 1

print(f'Notas de 50: {notas50}\nNotas de 20: {notas20}\nNotas de 10: {notas10}\nMoedas de 1: {notas1}\n')