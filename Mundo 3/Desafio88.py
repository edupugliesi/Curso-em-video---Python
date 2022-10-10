'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrado tudo em uma lista composta
'''
from random import randint
from time import sleep

numero = 0
qtde = int(input('Quantos palpites? '))
palpites = []
jogos = []


while qtde != 0:
    count = 0 # Contador da quantidade de números sorteado em cada palpite.   
    while True:
        numero = randint(1, 60)

        # Inserir números aleatórios, sem repetir, na list palpites.
        if numero not in palpites:
            palpites.append(numero)
            count += 1

        # Parar While
        if count >= 6:
            break
        
    palpites.sort()
    jogos.append(palpites[:]) # Inserir todos os palpites dentro da lista jogos.
    palpites.clear()
    
    qtde -= 1


# Printar todos os palpites dentro da lista jogos
for i, l in enumerate(jogos):
    print(f'{i + 1}º jogo: {l}')
    
sleep(1)
print('Boa sorte!')
        