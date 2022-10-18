'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número do dado.
'''
from random import randint
from operator import itemgetter

# Declaração da lista e dos números aleatórios para cada jogador
jogadores = {}
jogadores['Jogador1']=randint(1, 6)
jogadores['Jogador2']=randint(1, 6)
jogadores['Jogador3']=randint(1, 6)
jogadores['Jogador4']=randint(1, 6)

print('='*30)

# Printar os números sorteados para cada jogador
print('Sorteio: \n')
for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado')

# Colocar os jogadores em ordem de acordo com o número tirado
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('='*30)

# Printar vencedores em ordem
print('Vencedores: \n')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    
    

