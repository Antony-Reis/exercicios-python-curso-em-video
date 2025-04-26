"""Módulo que contem funções para rotinas"""

def linhas():
    """
    Imprime uma linha com os carateres - e =
    Ex :
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def escrever_linha(txt):
    txt = str('    '+txt+'    ').upper()
    texto_pronto = len(txt)*'='+'\n'+txt+'\n'+'='*len(txt)
    return texto_pronto

def e_par(num):
    if num % 2 ==0:
        return True
    else:
        return False

def e_impar(num):
    if num %2 != 0:
        return True
    else:
        return False

def ano_atual():
    from datetime import datetime
    return datetime.now().strftime("%Y")

def sair_qualquer_momento(string='Digite algo ou [SAIR]: '):
    from sys import exit as ex

    comando = input(string).lower().strip()
    if comando == 'sair':
        return ex('Encerrando o programa...')
    else:
        return  comando
