#Faça um programa que leia um número de 0 a 9999 e moestre na tela cada um dos dígitos separados

#Ex: Digite um número: 1834

#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

nome = str(input('\nQual o seu nome? ')).strip()
numero = int(input('Insira um número de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('\nOlá {}, o número digitado foi {} \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(nome, numero, unidade, dezena, centena, milhar))