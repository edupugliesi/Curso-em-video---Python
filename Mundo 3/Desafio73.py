'''
Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados.
B - Os ultimos 4 colocados
C - Uma lista com os times em ordem alfabética
D - Em que posição na tabela está o time do Palmeiras.
'''

print('-'*30)
print('TABELA DO BRASILEIRÃO 2022')
print('-'*30)

times = ('Palmeiras', 'Internacional', 'Fluminense', 
         'Flamengo', 'Corinthians', 'Athletico-PR', 
         'Atlético-MG', 'América-MG', 'Goiás', 
         'São Paulo', 'Botafogo', 'Santos', 
         'Bragantino', 'Fortaleza', 'Ceará SC', 
         'Coritiba', 'Avaí', 'Cuiabá', 
         'Atlético-GO', 'Juventude')

print(f'\nOs primeiros 5 colocados são: {times[0:6]}')
print(f'\nOs últimos 4 colocados são: {times[-4:]}')
print(f'\nOs times em ordem alfabética são: {sorted(times)}')
print(f'\nO time do Palmeiras se encontra em {times.index("Palmeiras") + 1}º colocado')