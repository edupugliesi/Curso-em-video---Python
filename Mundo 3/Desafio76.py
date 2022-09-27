'''
Crie um programa que tenha uma tupla única com nomes e produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em uma forma tabular.
'''

tupla = ('Caderno', 2.50, 'Caneta', 1.25, 'Borracha', 2.30, 'Lapis', 1.45, 'Apontador', 1.15)
count = 0

for lista in tupla:
    print(f'{tupla[0 + count]}...............R${tupla[1 + count]}')
    count += 2
