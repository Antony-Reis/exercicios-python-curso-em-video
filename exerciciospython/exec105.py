def notas(*num, sit=False):
    """
    Função para calcular o maior, menor e a media dos valores
    :param num: recebe os números para interar sobre, prefenencia de lista
    :param sit: informa a situação da turma, media >= 6 = boa, media < 6 = ruim
    :return: retorna um dicionário com todos as informações. sit=True para retornar a situação
    """
    l = list(num)
    dc = {
        'total':len(l),'maior':max(l),'menor':min(l),'media':round(sum(n for n in l)/len(l),2)
    }
    if sit:
        if dc['media'] >= 6:
            dc['situacao'] = 'BOA'
        elif dc['media'] < 6:
            dc['situacao'] = 'RUIM'

    return dc

print(notas(10,9,4,3,5,3,1, sit=True))