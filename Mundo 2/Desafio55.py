'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos'''

print('-'*30)

maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
    peso = float(input('Insira o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
        
print('-'*30)

print('O menor peso é {}KG.'.format(menorPeso))
print('O maior peso é {}KG.'.format(maiorPeso))
    