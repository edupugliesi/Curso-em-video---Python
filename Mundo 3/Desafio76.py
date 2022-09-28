'''
Crie um programa que tenha uma tupla única com nomes e produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em uma forma tabular.
'''

tupla = ('Caderno', 2.50, 'Caneta', 1.25, 'Borracha', 2.30, 'Lapis', 1.45, 'Apontador', 1.15)
count = 0

print('-'*50)

for lista in range(0, len(tupla)):
    if lista % 2 == 0:
        print(f'{tupla[lista]:.<30}', end='')
    else:
        print(f'R${tupla[lista]:>7.2f}')
    
print('-'*50)
print('Fim')
