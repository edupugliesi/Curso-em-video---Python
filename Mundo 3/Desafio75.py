'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No fina mostre:

A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o primeiro número 3
C - Quais foram os números pares
'''

tupla = (int(input('Digite o 1º número: ')), 
         int(input('Digite o 2º número: ')), 
         int(input('Digite o 3º número: ')), 
         int(input('Digite o 4º número: ')))

print(f'Os valores digitados foram {tupla}')

print(f'O número 9 aparece {tupla.count(9)} vezes.') #Mostra quantas vezes aparece o número 9 na Tupla
if 3 in tupla:
    print(f'O número 3 aparece primeiramente na {tupla.index(3) + 1}º posição') #Mostra em qual posição está o número 3
else:
    print('Número 3 não digitado na Tupla!')

print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 ==0:
        print(n, end=' ')
print('\nFim')