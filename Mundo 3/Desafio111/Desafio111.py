'''
Crie um pacote que chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo
funcionando.
'''

from ulitidadesCeV import moeda, titulo, dado

titulo.titulo('Desafio111 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))
taxa = float(input('Digite a taxa (%): '))

moeda.resumo(valor, taxa)