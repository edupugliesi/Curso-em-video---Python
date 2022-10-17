'''
Crie um programa que leia nome. ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a ctps for diferente de ZERO, o dicionário receberá tambpem o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime

print('='*30)

trabalhador = {}
trabalhadores = []

while True:
    trabalhador['nome'] = str(input('Nome: '))
    anoDeNascimento = int(input('Ano de Nascimento: '))
    trabalhador['idade'] = datetime.now().year - anoDeNascimento
    trabalhador['carteira de trabalho'] = int(input('Carteira de Trabalho (0 caso não houver): '))
    
    if trabalhador['carteira de trabalho'] != 0:
        trabalhador['ano de contratação'] = int(input('Ano de contratação: '))
        trabalhador['salário'] = int(input('Salário: '))
        trabalhador['aposentadoria (idade)'] = (trabalhador['ano de contratação']- anoDeNascimento) + 35
    
    trabalhadores.append(trabalhador.copy())
    trabalhador.clear()
    
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
    if op == 'N':
        print('='*30)
        break
    
    print('-'*30)

for t in trabalhadores:
    for k, v in t.items():
        print(f'# {k}: {v}')
    print('-'*30)
