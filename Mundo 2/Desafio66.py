'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles!
Desconsiderando o FLAG.
'''

n = 0
soma = 0
count = 0
while True:
    count += 1
    n = int(input(f'Insira o {count}° número: '))
    
    if n == 999:
        count -= 1
        break
    
    soma += n
    
print(f'A soma dos {count} números inseridos é {soma}')
    