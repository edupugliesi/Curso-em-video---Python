'''
Crie um programa qeu vai gerar 5 nmúmeros aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor em questão na Tupla.
'''

from random import randint

print('-'*30)

tupla = (randint(0, 10), randint(0, 10), 
         randint(0, 10), randint(0, 10), 
         randint(0, 10))

print(f'Os números gerados foram {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')


