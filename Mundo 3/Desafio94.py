'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:

A - Quantas pessoas foram cadastradas.
B - A média de idade do grupo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média

'''
print('='*30)

pessoa = {}
grupo = []
mulheres = []

count = 1

while True:
    print(f'\n-- {count}º pessoa --\n')
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo: ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    
    
    grupo.append(pessoa.copy())
    
    op = str(input('Deseja continuar? [S/N]: ' )).strip().upper()
    if op == 'N':
        print('='*30)
        break
    
    count += 1
    print('-'*30)

print(grupo)

print(f'Foram cadastrados {len(grupo)} pessoas')
