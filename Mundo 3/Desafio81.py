'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A - Quantos números foram digitados
B - A lista de valores, ordenada de forma decrescente
C - Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
count = 1
op = ''

while True:
    lista.append(int(input(f'Digite o {count}º número: ')))
    count += 1
        
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if op != 'S':
        break
    
print('\n' + '*'*30 + '\n')

# Print para mostar quantos números foram inseridos na Lista!
print(f'Foram digitandos {len(lista)} números!')

# IF para validar se o número 5 foi inserido na Lista
if 5 in lista:
    print(f'Número 5 foi digitado e aparece primeiramente no {lista.index(5)}º índice da lista.')
else:
    print('Número 5 não foi digitado!')

# Print da lista em ordem decrescente.
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são: {lista}')


