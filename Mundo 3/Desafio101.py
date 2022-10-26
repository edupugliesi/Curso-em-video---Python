'''
Crie um programa que tenha uma função chamada voto() que vai receber  como parâmetro o ano de nascimento
de uma pessoa, retornando o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONMAL ou OBRIGATÓRIO
nas eleições
'''

from datetime import datetime

def texto(msg):
    print()
    print('#'*len(msg))
    print(msg)
    print('#'*len(msg))
    print()

def voto(anoNascimento):
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        texto(f'{nome}, você tem {idade} anos, portanto seu voto é proibido')
    elif idade >= 16 and idade < 18:
        texto(f'{nome}, você tem {idade} anos, portanto seu voto é opcional')
    elif idade >= 18 and idade < 60:
        texto(f'{nome}, você tem {idade} anos, seu voto obrigatório')
    elif idade > 60:
        texto(f'Sr.(a) {nome}, você tem {idade} anos, seu voto é opcional')

nome = str(input('\nQual o seu nome? '))
voto(int(input('Qual ano você nasceu? ')))