'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior
'''

from random import randint

def mensagem(msg):
    print()
    print('*'*len(msg))
    print(msg)
    print('*'*len(msg))
    print()
    
lista = []
def sorteia():
    mensagem('Sorteando números')
    numero = 0
    for n in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Números sorteados: {lista}')

def somaPar():
    mensagem('Somando todos os números pares sorteados!')
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os números pares sorteados é {soma}')

sorteia()
somaPar()