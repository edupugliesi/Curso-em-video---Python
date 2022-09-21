'''
Faça um programa que leia um número qualquer e mostre seu fatorial

Ex: 5! = 5x4x3x2x1 = 120
'''

from math import factorial

numero = int(input('Digite um número para calcular o seu fatorial: '))
count = numero
fat = 1
print('{}! = '.format(numero), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat = fat * count
    count = count - 1
        


print('{}'.format(fat))