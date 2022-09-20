'''
Faça um programa que leia um número qualquer e mostre seu fatorial

Ex: 5! = 5x4x3x2x1 = 120
'''

n = int(input('Insira um número inteiro qualquer e lhe darei o seu fatorial: '))
count = n
fat = 0
r = 0


while count != 0:
    fat = n * (n - 1)
    count -= 1
    print(count, fat)
print('O fatorial de {} é {}'.format(n, fat))