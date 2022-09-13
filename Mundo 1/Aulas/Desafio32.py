#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

nome = str(input('\nQual seu nome? '))
ano = int(input('Informe um ANO, e lhe direi se ele é BISSEXTO: '))

if ano % 4 == 0:
    print('{}, o ano de {} representa um ano BISSEXTO!\n'.format(nome, ano))
if ano % 4 != 0:
    print('{}, o ano de {} não representa um ano BISSEXTO!\n'.format(nome, ano))
