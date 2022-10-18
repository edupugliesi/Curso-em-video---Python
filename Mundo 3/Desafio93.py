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


jogador['nome'] = str(input('Nome do jogador: ')) # Input nome do jogador direto no dicionário
qtdeJogos = int(input('Quantos jogos jogou? ')) # Input da quantidade de jogos
jogador['jogos']=qtdeJogos # Quantidade de jogos no dicionário

# While com base na quantidade de jogos
while qtdeJogos != 0:
    
    gols = int(input(f'Quantos gols feitos na {count}º partida? '))
    TotalGols.append(gols) # Input dos gols em cada partida na lista 
    
    # Contadores
    qtdeJogos -= 1
    count += 1

# Soma total de gols na partida
for gol in TotalGols:
    somaGols += gol
jogador['total de gols'] = somaGols

print('-'*30)
# Printar dados na tela
for k, v in jogador.items():
    print(f'{k}: {v}')
    
print(TotalGols)