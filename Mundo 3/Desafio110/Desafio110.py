'''Adicione ao módulo da moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado ate aqui.
'''

from Modulos110 import moeda, titulo

titulo.titulo('Desafio110 - Manipulação de valores')

valor = float(input('Digite um valor (R$): '))
taxa = int(input('Digite a taxa (%): '))
moeda.resumo(valor, taxa)