'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''

print('-'*30)

print('Digite um número e vamos ver se ele é um número primo!')

numero = int(input('Insira um número: '))
count = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível for {} vezes'.format(numero, count))

if count == 2:
    print('O número {} é um número primo!'.format(numero))
else:
    print('O número {} não é um número primo!'.format(numero))