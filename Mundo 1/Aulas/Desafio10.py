#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

#Considerar US$1,00 = R$5,15

nome = str(input('\nOlá, qual o seu nome?\n'))
real = float(input('\nQuanto dinheiro você tem na carteira?\n'))

print('\n{}, R${} da pra comprar aproximadamente US${:.2f}\n'.format(nome, real, real/5.15))