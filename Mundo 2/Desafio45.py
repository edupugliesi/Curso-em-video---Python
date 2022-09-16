#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('-'*30)
print('Vamos jogar Jokenpô?')
nome = str(input('Qual o seu nome? '))
print('-'*30)
jogador = int(input('1 = PEDRA \n2 = PAPEL \n3 = TESOURA \n'))

computador = randint(1, 3)

print('-'*30)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO \n')


#Solução sem usar IF dentro de IF.

if computador == 1 and jogador == 2:
    print('O computador escolheu PEDRA e {} escolheu PAPEL. Você ganhou'.format(nome))
elif computador == 2 and jogador == 1:
    print('O computador escolheu PAPEL e {} escolheu PEDRA. Você perdeu'.format(nome))
elif computador == 1 and jogador == 3:
    print('O computador escolheu PEDRA e {} escolheu TESOURA. Você perdeu'.format(nome))
elif computador == 3 and jogador == 1:
    print('O computador escolheu TESOURA e {} escolheu PEDRA. Você ganhou'.format(nome))
elif computador == 2 and jogador == 3:
    print('O computador escolheu PAPEL e {} escolheu TESOURA. Você ganhou'.format(nome))
elif computador == 3 and jogador == 2:
    print('O computador escolheu TESOURA e {} escolheu PAPEL. Você perdeu'.format(nome))
elif computador == jogador:
    print('EMPATE'.format(nome))