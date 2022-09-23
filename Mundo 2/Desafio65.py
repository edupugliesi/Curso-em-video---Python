'''
Crie um programa que leia vários números inteiros pelo teclado.
No final mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

print('-'*30)

print('')
count = 0
numero = 0
media = 0
maiorValor = 0
menorValor = 0
soma = 0
op = 'S'

while op != 'N':
    count += 1
    numero = int(input('Digite o {}º valor: '.format(count)))
    soma += numero
    media = soma / count
    if numero > maiorValor:
        maiorValor = numero
    elif numero < menorValor:
        menorValor = numero
    op = str(input('Deseja continuar digitando valores? [S/N] ')).strip().upper()
    print('='*30)

print('Foram digitados {} valores e a média entre eles é {}'.format(count, media))
print('Fim')
    