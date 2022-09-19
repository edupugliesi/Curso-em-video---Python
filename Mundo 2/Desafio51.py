'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA, no final mostre os 10 primeiros termos dessa progressão'''

print('-'*30)

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razao

for c in range(primeiroTermo, decimoTermo + razao, razao):
    print(c, end=' => ')
print('Fim')
    