'''
Adapte o código do desafio107, criando uma função adicional chamada moeda(), que consiga mostrar
os valores como um valor monetário formatado
'''

from Modulos import moeda, titulo

titulo.titulo('Desafio107 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))

print(moeda.aumentar(moeda.moeda(valor)))
print(moeda.diminuir(moeda.moeda(valor)))
print(moeda.dobro(moeda.moeda(valor)))
print(moeda.metade(moeda.moeda(valor)))
