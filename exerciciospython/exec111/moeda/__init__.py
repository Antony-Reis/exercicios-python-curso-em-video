from exerciciospython import funcoes
def moeda(num):
    num = float(num)
    numf = f'${num:.2f}'.replace('.', ',')
    return numf

def dobro(num, moedaf=False):
    n = num*2
    if moedaf:
        n = moeda(n)
        return n
    else: return n

def metade(num, moedaf=False):
    n = round(num / 2,2)
    if moedaf:
        n = moeda(n)
        return n
    else: return n

def aumentar(num, porcentagem, moedaf=False):
    n = (num*(porcentagem/100))+num
    if moedaf:
        n = moeda(n)
        return n
    else: return n

def diminuir(num, porcentagem, moedaf=False):
    n = num - (num*(porcentagem/100))
    if moedaf:
        n = moeda(n)
        return n
    else: return n

def resumo(num, porcentagem_aumento, porcentagem_diminuicao):
    funcoes.linhas()
    print('RESUMO DO VALOR')
    funcoes.linhas()
    print(f'Preço analisado: {moeda(num)}\nDobro do valor: {dobro(num, moedaf=True)}\nMetade do valor: {metade(num, moedaf=True)}\n{porcentagem_aumento}% de aumento: {aumentar(num, porcentagem_aumento, moedaf=True)}\n{porcentagem_diminuicao}% de redução: {diminuir(num, porcentagem_diminuicao, moedaf=True)}')
    funcoes.linhas()