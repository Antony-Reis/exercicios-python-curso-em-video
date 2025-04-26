nome = input('Insira seu nome todo: ')
nome = nome.title()
nomelist = nome.split()

print(f'Nome : {nome}\nPrimeiro nome: {nomelist[0]}\nUltimo nome: {nomelist[len(nomelist)-1]}')