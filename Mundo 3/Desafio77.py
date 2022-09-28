'''
Crie um programa que tenha uma tupla com várias palavras(Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

carnes = ('acem', 'mignon', 'picanha', 
         'alcatra', 'coxaomole', 'coxaoduro', 
         'musculo', 'patinho', 'maminha', 
         'fraldinha', 'costela', 'cupim')

for delicia in carnes:
    print(f'\nNa carne {delicia.upper()} temos ', end='')
    for letra in delicia:
        if letra.lower() in 'aeiou':
            print(letra, end='')