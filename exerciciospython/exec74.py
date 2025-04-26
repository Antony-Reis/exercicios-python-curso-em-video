from random import randint
num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
lista = []

for n in num:
    lista.append(str(n))

print(f'Os números gerados foram: {", ".join(lista)}.\nO menor deles é {min(num)} e o maior deles é {max(num)}.')