#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random


numSecreto = random.randint(0,5)

nome = str(input('Olá, qual o seu nome? '))
numTentativa = int(input('\nVamos jogar um jogo, tente adivinhar o número secreto. Insira um número de 0 a 5: '))

if numTentativa > 5:
    print('Você inseriu um número maior que 5.\n')
if numTentativa < 0:
    print('Você inseriu um número negativo!\n')
if numTentativa == numSecreto:
    print('Parabéns {}, você acertou. O número secreto era {} e você informou o número {} corretamente!\n'.format(nome, numSecreto, numTentativa))
else:
    print('Erôôôu. Computador wins!\n')