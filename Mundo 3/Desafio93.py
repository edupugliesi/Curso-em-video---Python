'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador, quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
print('='*30)

jogador = {}
gols = 0
TotalGols = []
somaGols = 0
count = 1

jogador['nome'] = str(input('Nome do jogador: '))
qtdeJogos = int(input('Quantos jogos jogou? '))
jogador['jogos']=qtdeJogos

while qtdeJogos != 0:
    
    gols = int(input(f'Quantos gols feitos na {count}º partida? '))
    TotalGols.append(gols)
    
    qtdeJogos -= 1
    count += 1

for gol in TotalGols:
    somaGols += gol
jogador['total de gols'] = somaGols

print('-'*30)
for k, v in jogador.items():
    print(f'{k}: {v}')
    
print(TotalGols)