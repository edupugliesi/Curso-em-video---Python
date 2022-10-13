'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número do dado.
'''
from random import randint

jogadores = {}
jogadores['Jogador1']=randint(1, 6)
jogadores['Jogador2']=randint(1, 6)
jogadores['Jogador3']=randint(1, 6)
jogadores['Jogador4']=randint(1, 6)

print(jogadores)
    
    

