'''
Adapte o código do desafio107, criando uma função adicional chamada moeda(), que consiga mostrar
os valores como um valor monetário formatado
'''

from Modulos108 import moeda, titulo

titulo.titulo('Desafio107 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))
taxa = int(input('Digite a taxa (%): '))

print(f'O valor aumentado em {taxa}% é {moeda.moeda(moeda.aumentar(valor, taxa))}')
print(f'O valor diminuído em {taxa}% é {moeda.moeda(moeda.diminuir(valor, taxa))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
