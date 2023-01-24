'''Reescreva a função leiaInt() que fizemos no Desafio104, incluindo agora a possibidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''

from Modulos113 import leiaFloat, leiaInt, titulo

titulo.titulo('Desafio 113 :D')

num = leiaInt.leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat.leiaFloat('Digite um valor real: ')

print(f'\nO valor inteiro digitado foi {num} e o número real foi {num2}')