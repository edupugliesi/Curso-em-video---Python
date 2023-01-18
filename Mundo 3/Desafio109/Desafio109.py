'''
Modifique as funções que foram criadas no desafio107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida
no desafio108
'''

from Modulos109 import moeda, titulo

titulo.titulo('Desafio109 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))
taxa = int(input('Digite a taxa (%): '))

print(f'O valor aumentado em {taxa}% é {moeda.moeda(moeda.aumentar(valor, taxa), format=True)}')
print(f'O valor diminuído em {taxa}% é {moeda.moeda(moeda.diminuir(valor, taxa), format=True)}')
print(f'O dobro de {moeda.moeda(valor, format=True)} é {moeda.moeda(moeda.dobro(valor), format=True)}')
print(f'A metade de {moeda.moeda(valor, format=True)} é {moeda.moeda(moeda.metade(valor), format=True)}') 