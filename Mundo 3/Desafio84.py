'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A - Quantas pessoas foram cadastradas
B - Uma listagem com as pessoas mais pesadas
C - Uma listagem com as pessoas mais leves
'''

pessoa = []
galera = []
maisPesados = []
maisLeves = []


while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Peso: ')))
    galera.append(pessoa[:])
    
    if len(galera) == 1:
        maisPesados.append(pessoa[:])
        maisLeves.append(pessoa[:])
    
    
        
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
    
    pessoa.clear()
    
    if op != 'S':
        print('='*30)
        break


print(f'{len(galera)} pessoas foram cadastradas!')

print(galera)