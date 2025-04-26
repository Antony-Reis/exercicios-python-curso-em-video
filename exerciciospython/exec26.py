frase = input('Insira uma frase: ')
frase = frase.replace('á','a').replace('ã','a').replace('â','a').replace(' ','')

print(f'Tem {frase.count("a")} As na frase\nEla aparece pela primeira vez na {frase.find("a")+1}° letra da frase\nE a ultima vez é na {frase.rfind("a")+1}° letra da frase')