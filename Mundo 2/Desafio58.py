'''
Melhore o jogo do Desafio28 onde o computador vai "PENSAR" em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer.


'''

import random


numSecreto = random.randint(0,10)

nome = str(input('Olá, qual o seu nome? '))
numTentativa = int(input('\nVamos jogar um jogo, tente adivinhar o número secreto. Insira um número de 0 a 5: '))

count = 0
while numTentativa != numSecreto:
    numTentativa = int(input('Erôôôu, tente novamente: '))
    count += 1
print('{}, você acertou. O número correto era {} e você precisou de {} tentativas para acertar!'.format(nome, numSecreto, count))
    