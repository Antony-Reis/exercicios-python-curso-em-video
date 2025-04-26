from time import sleep as sp
from funcoes import linhas

def contagem_personalizada(inicio, fim, passo):
    fimfor = fim + 1
    print(f'Contagem\nInicio: {inicio} -> Fim: {fim}\nPasso: {passo}')
    for i in range(inicio, fimfor, passo):
        print(i, end=' ')
        sp(1)
    print()

def contagem_personalizada_reversa(inicio, fim, passo):
    fimfor = fim + 1
    print(f'Contagem\nInicio: {fim} -> Fim: {inicio}\nPasso: {passo}')
    for i in range(inicio, fimfor, passo):
        print(10-i, end=' ')
        sp(1)
    print()



linhas()
contagem_personalizada(0, 10,1)
linhas()
contagem_personalizada_reversa(0, 10, 2)
linhas()
contagem_personalizada(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
linhas()