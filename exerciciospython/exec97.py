def escrever_linha(txt):
    txt = str('    '+txt+'    ').upper()
    texto_pronto = len(txt)*'='+'\n'+txt+'\n'+'='*len(txt)
    return texto_pronto
while True:
    texto = input('Insira um texto qualquer:\n')
    if texto == 'sair':
        print('Programa encerrado')
        break
    print(escrever_linha(texto))