'''
Crie um programa que leia vários números inteiro pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

PS: Desconsiderar o FLAG 999.
'''

print('='*30)

numero = 0
soma = 0
count = 0

while numero != 999:
    numero = int(input('Digite um número inteiro ou (999) para parar: '))
    soma += numero
    if numero == 999:
        soma = soma - 999
        count -= 1
    count += 1
print('Você digitou {} numeros e a soma deles é {}'.format(count, soma))