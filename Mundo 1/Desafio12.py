#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

nome = str(input('\nQual o seu nome? '))
produto = str(input('Qual o produto? '))
valor = float(input('Qual o preço do(a) {}? '.format(produto)))

desconto = (valor * 0.05)
valorFinal = valor - desconto

print('{}, o {} custa R${} e tem R${} de desconto. O valor final do {} desce para R${}.'.format(nome, produto, valor, desconto, produto, valorFinal))