'''
FAça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores'''

def ajuda(com):
    help(com)
    
def titulo(msg, cor=0):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)

comando = ''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo')