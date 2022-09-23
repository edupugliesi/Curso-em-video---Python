'''
Crie um programa que leia idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
A - Quantas pessoas tem mais de 18 anos
B - Quantos homens foram cadastrados
C - Quantas mulheres tem menos de 20 anos
'''

idade = 0
maior18 = 0
sexo = ''
sexoMasculino = 0
mulheresAbaixo20Anos = 0
count = 0
op = ''

while True:
    count += 1
    print('-'*30)
    print(f'{count}º pessoa')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    
    op = str(input('\nDeseja cadastrar outra pessoa? [S/N]: ')).strip().upper()
    
    if idade >= 18:
        maior18 += 1
        
    if sexo == 'M':
        sexoMasculino += 1
        
    if sexo == 'F' and idade < 20:
        mulheresAbaixo20Anos += 1
        
    if op == 'N':
        print('='*30)
        break
        

print(f'Foram cadastrados {maior18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {sexoMasculino} homens.')
print(f'Foram cadastradas {mulheresAbaixo20Anos} mulheres com menos de 20 anos.')