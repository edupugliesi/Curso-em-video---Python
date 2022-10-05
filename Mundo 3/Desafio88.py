'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrado tudo em uma lista composta
'''
from random import randint

qtde = int(input('Quantos palpites? '))
palpites = []
jogos = []

while qtde != 0:
    for c in range(0, 6):
        palpites.append(randint(1, 60))
        jogos.append(palpites[:][0])
        palpites.clear()

    qtde -= 1

print(jogos)
        