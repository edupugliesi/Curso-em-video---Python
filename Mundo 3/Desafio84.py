'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A - Quantas pessoas foram cadastradas
B - Uma listagem com as pessoas mais pesadas
C - Uma listagem com as pessoas mais leves
'''

print('='*30)

pessoa = []
galera = []
maisPesado = 0
maisLeve = 0


while True:
    #Adiciona a pessoa e seu peso na lista pessoa
    pessoa.append(str(input('Nome: '))) 
    pessoa.append(float(input('Peso: ')))
    
    
    if len(galera) == 0:
        maisPesado = maisLeve = pessoa[1]
    else:
        if pessoa[1]> maisPesado:
            maisPesado = pessoa[1]
        elif pessoa[1] < maisLeve:
            maisLeve = pessoa[1]
    
    
    galera.append(pessoa[:]) # Cria uma cópia da Lista Pessoa na lista Galera
    pessoa.clear() # Limpa a lista pessoa
        
        
    # Operação para parar a repetição
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
    
    if op != 'S':
        print('='*30)
        break
    
    print('-'*30)

print(f'{len(galera)} pessoas foram cadastradas!')
print(f'O maior peso foi {maisPesado}. Os mais pesados foram: ', end='')

for p in galera:
    if p[1] == maisPesado:
        print(f'{p[0]}... ', end='')

print()

print(f'O menor peso foi {maisLeve}. Os mais leves foram: ', end='')

for p in galera:
    if p[1] == maisLeve:
        print(f'{p[0]}... ', end='')

print()