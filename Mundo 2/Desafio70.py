'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:
A - Qual o total gasto na compra
B - Quantos produtos custam mais de R$1000,00
C - Qual é o nome do produto mais barato'''

print('='*30)
print('LOJINHA DO DUDU')
print('='*30)

produto = ''
preco = 0
total = 0
produtoMaisDe1000Reais = 0
produtoMaisBarato = ''
valorProdutoMaisBarato = 0
op = ''

while True:
    produto = str(input('\nInsira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    op = str(input('Mais algum produto? [S/N] ')).strip().upper()
    total += preco
    valorProdutoMaisBarato = preco
    produtoMaisBarato = produto
    
    if preco > 1000:
        produtoMaisDe1000Reais += 1
    if preco < valorProdutoMaisBarato:
        valorProdutoMaisBarato = preco
        produtoMaisBarato = produto
    if op == 'N':
        break
    
print("+"*50)
print(f'O total da compra foi R${total}')
print(f'{produtoMaisDe1000Reais} produtos custaram mais de R$1000,00.')
print(f'O produto mais barato é {produtoMaisBarato}')
    