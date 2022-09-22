'''
Escreva um programa que leia um N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência de Fibonacci.

Ex:
0 1 1 2 3 5 8
'''
print('='*30)

termos = int(input('Digite quantos termos quer mostrar da sequência de Fibonacci: '))
termo1 = 0
termo2 = 1

print('{} > {}'.format(termo1, termo2), end='')

count = 3

while count <= termos:
    termo3 = termo1 + termo2
    print(' > {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    count += 1
    
print(' > FIM')
    