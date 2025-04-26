from exerciciospython.exec111.dados import leia_dinheiro
from exerciciospython.exec111.moeda import resumo

num = leia_dinheiro('Insira um valor: ')
porce_aumen = int(input('Insira a porcentagem de aumento: '))
porce_redu = int(input('Insira a porcentagem de diminuição: '))

resumo(num, porce_aumen, porce_redu)