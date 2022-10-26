'''
Faça um programa que tenha uma função chamada ficha(), que receba dos parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
'''

def texto(msg):
    linha = len(msg) + 4
    print()
    print('-' * linha)
    print(f'  {msg}')
    print('-' * linha)
    print()

def ficha(nome = ' ', gols = 0):
    texto('Jogador')
    print(f'Jogador: {nome}')
    print(f'Gols: {gols}')

texto(f'Ficha do jogador')
ficha(str(input('Jogador: ')), int(input('Gols: ')))