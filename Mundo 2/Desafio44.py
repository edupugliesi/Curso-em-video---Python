#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento

#A vista dinheiro/cheque: 10% de desconto
#A vista cartão: 5% de desconto
#Em até 2x no cartão: Preço normal
#Em 3x ou mais no cartão: 20% de juros

print('-'*30)

nome = str(input('Qual o seu nome? '))
preco = float(input('Qual o preço do produto? '))

formaDePagamento = int(input('\nQual a forma de pagamento? \n0 = A vista no dinheiro/cheque \n1 = A vista no cartão \n2 = 2x sem juros \nOu adicione em quantas vezes quer pagar com 20% de juros ao mês! '))


if formaDePagamento == 0:
    total = preco - (preco * 0.10)
    print('{}, o produto custa R${:.2f} e seu preço a vista em dinheiro/cheque fica R${:.2f}'.format(nome, preco, total))
elif formaDePagamento == 1:
    total = preco - (preco * 0.05)
    print('{}, o produto custa R${:.2f} e seu preço a vista no cartão fica R${:.2f}'.format(nome, preco, total))
elif formaDePagamento == 2:
    total = preco / 2
    print('{}, o produto custa R${:.2f} e seu preço dividido em 2x no cartão fica R${:.2f} por mês!'.format(nome, preco, total))
elif formaDePagamento >= 3:
    parcela = (preco / formaDePagamento)
    total = (parcela * 0.20) + parcela
    print('{}, o produto custa R${:.2f} e seu preço dividido em {}x no cartão fica R${:.2f} por mês'.format(nome, preco, formaDePagamento, total))

