#Crie um programa que leia um número Real qualquer pelo tecaldo e mostre na tela sua porção inteira.
#Ex: Número 6.127. Parte inteira 6.

from math import trunc

nome = str(input('Qual o seu nome? '))
n = float(input('Insira um número: '))

print('Olá {}, o número digitado foi {} e sua parte inteira é {}!'.format(nome, n, trunc(n)))

# Resolução sem usar a biblioteca math.
print('Olá {}, o número digitado foi {} e sua parte inteira é {}!'.format(nome, n, int(n)))