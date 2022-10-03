'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
parentesesAberto = []
parentesesFechado = []

# Procura os parênteses existentes na expressão
for parenteses in expressao:
    # Se encontrar um parênteses abrindo, adiciona um parêntes aberto na lista parentesesAberto = []
    if parenteses == '(':
        parentesesAberto.append('(')
        
    # Se encontrar um parênteses fechando, adiciomna um parênteses fechado na lista parentesesFechado = []
    elif parenteses == ')':
        parentesesFechado.append(')')

# IF para comparar se a quantidade de parêntes abertos e fechados nas respectivas listas são iguais.
if len(parentesesAberto) == len(parentesesFechado):
    print('Sua expressão está correta!')

# IF para comparar se a quantidade de parêntes abertos e fechados nas respectivas listas são diferentes.
elif len(parentesesAberto) != len(parentesesFechado):
    print('Sua expressão está errada!')
        
        