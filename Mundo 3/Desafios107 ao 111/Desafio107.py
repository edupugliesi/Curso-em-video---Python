'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções
'''

from Modulos import moeda, titulo

titulo.titulo('Desafio107 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))

print(moeda.aumentar(valor))
print(moeda.diminuir(valor))
print(moeda.dobro(valor))
print(moeda.metade(valor))