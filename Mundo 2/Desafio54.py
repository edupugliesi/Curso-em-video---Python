'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores
'''
from datetime import date

print('-'*30)

maiorDeIdade = 0
menorDeIdade = 0

for c in range(1, 8):
    ano = int(input('Qual ano a {}º pessoa nasceu? '.format(c)))
    if date.today().year - ano >= 18:
        maiorDeIdade =+ 1
    elif date.today().year - ano < 18:
        menorDeIdade =+ 1
        
print('-'*30)
        
print('{} pessoas são maiores de idade!'.format(maiorDeIdade))
print('{} pessoas são menores de idade!'.format(menorDeIdade))