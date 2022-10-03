'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
parentesesAberto = []
parentesesFechado = []

for parenteses in expressao:
    if parenteses == '(':
        parentesesAberto.append('(')
    elif parenteses == ')':
        parentesesFechado.append(')')
    
if len(parentesesAberto) == len(parentesesFechado):
    print('Sua expressão está correta!')
elif len(parentesesAberto) != len(parentesesFechado):
    print('Sua expressão está errada!')
        
        