'''
Aprimore o Desafio93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.
'''

print('='*30)

jogador = {}
jogadores = []
gols = 0
TotalGols = []
somaGols = 0
count = 1
countJogador = 1




while True:
    jogador.clear() # Limpar dicionário jogador para inserir um novo jogador
    TotalGols.clear() # Limpar lista de gols para receber uma nova lista de gols
    somaGols = 0 # Zerando a soma de gols para uma nova soma.
    
    print(f'\n{countJogador}º jogador \n') # Print com a posição do jogador
    
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip() # Input nome do jogador direto no dicionário
    qtdeJogos = int(input('Quantos jogos jogou? ')) # Input da quantidade de jogos
    jogador['jogos']=qtdeJogos # Quantidade de jogos no dicionário
    
    # While com base na quantidade de jogos (Contagem de gols)
    while qtdeJogos != 0:
        
        gols = int(input(f'- Quantos gols feitos na {count}º partida? '))
        TotalGols.append(gols) # Input dos gols em cada partida na lista 
        
        # Soma dos gols
        somaGols += gols
        jogador['total de gols'] = somaGols
        
        # Input a lista de gols no dicionário jogador
        jogador['saldo de gols'] = TotalGols[:]
        
        # Contadores
        qtdeJogos -= 1
        count += 1

    
    jogadores.append(jogador.copy()) # Adicionando uma cópia do dicionário jogador na lista jogadores
    
    count = 1 # Retornando o contador de partidas para uma nova contagem
    countJogador += 1 # Contador da quantidade de jogadores adicionados
        
    # Operação para encerrar o programa com validação de opção S ou N.
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while op not in 'SN':
        op = str(input('Opção Inválida, insira S ou N: ')).upper().strip()
            
    if op == 'N':
        print('='*30)
        break

# Printar dados na tela
for p in jogadores:
    for k, v in p.items():
        print(f'{k}: {v}')
    print('-'*30)
