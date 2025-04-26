import random
from random import choice

opcoes = ['Pedra', 'Papel', 'Tesoura']
print('Vamos jogar um pedra, papel, tesoura!\n'+33*'=')
while True:
    escolhahumana = input('Escolha: pedra, papel, tesoura\n').capitalize()
    escolharobo = random.choice(opcoes)

    if escolhahumana not in opcoes:
        print('Escolha inválida, Tente novamente\n')
        continue

    print(f"\nVocê escolheu: {escolhahumana}")

    print(f"Robo escolheu: {escolharobo}")

    # Dicionário com as regras do jogo
    regras = {
            'Pedra': 'Tesoura',
            'Tesoura': 'Papel',
            'Papel': 'Pedra'
        }

    if escolhahumana == escolharobo:
        print("Empate! 🤝\n")
        break

    elif regras[escolhahumana] == escolharobo:
        print("Você venceu! 🎉\n")
        break

    else:
        print("Você perdeu! 😢\n")
        break