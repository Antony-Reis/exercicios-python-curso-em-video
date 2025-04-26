expresao = input('Vamos verficar o parentese\nInsira uma expressão: ')
abertos = expresao.count('(')
fechados = expresao.count(')')

print('A expressão está com os parénteses corretos' if abertos == fechados else 'A expressão não está com os parénteses corretos')