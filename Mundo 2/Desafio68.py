'''
Faça um programa que jogue Par ou Impar com o computador.
O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from imaplib import Int2AP
from random import randint

print('-'*30)
print('PAR ou ÍMPAR')
print('-'*30)

player = 0
vitorias = 0
computador = 0
soma = 0
resultado = 0
op = ''

while True:
    computador = randint(0, 5)
    player = int(input('Insira um número inteiro de 0 a 5: '))
    op = str(input('PAR ou IMPAR? ')).upper().strip()
    soma = computador + player
    resultado = soma % 2
    
    #print(computador, player, soma, resultado, vitorias, op)
    
    if op == 'PAR' and resultado == 0 or op == 'IMPAR' and resultado >= 1:
        print('='*30)
        print(f'O computador escolheu {computador} e você {player}. A soma é {soma}. Você ganhou!')
        vitorias += 1
    
    elif soma == 0:
        print('Ambos colocaram 0, joguem novamente!')
        
    else:
        print('='*30)
        print(f'O computador escolheu {computador} e você {player}. A soma é {soma}. Você perdeu!')
        break

print('='*30)
print(f'Você ganhou {vitorias} vezes consecutivas!')  