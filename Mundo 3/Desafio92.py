'''
Crie um programa que leia nome. ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a ctps for diferente de ZERO, o dicionário receberá tambpem o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

print('='*30)

trabalhador = {}
trabalhadores = []

while True:
    

    trabalhador['nome'] = str(input('Nome: '))
    anoDeNascimento = int(input('Ano de Nascimento: '))
    trabalhador['idade'] = 2022 - anoDeNascimento
    trabalhador['carteira de trabalho'] = int(input('Carteira de Trabalho: '))
    
    if trabalhador['carteira de trabalho'] > 0:
        trabalhador['ano de contratação'] = int(input('Ano de contratação: '))
        trabalhador['salário'] = int(input('Salário: '))
        trabalhador['aposentadoria (idade)'] = trabalhador['idade'] + 35
    
    trabalhadores.append(trabalhador.copy())
    
    op = str(input('Deseja continuar? [S/N]')).strip().upper()
    
    if op == 'N':
        print('='*30)
        break
    
    print('-'*30)

print(trabalhador)
