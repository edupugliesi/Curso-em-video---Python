'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
Se o valor digitado for impar, desconsidere-o.
'''
print('='*30)
s = 0
count = 0

for c in range(1, 7):
    n = int(input('Digite o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        count += 1
print('A soma dos {} números pares digitados são {}'.format(count, s))