'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
'''
print('-'*30)

numeroMaior = 0 
numeroMenor = 0
lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite o {c}º número: ')))

    # Se for o primeiro número digitado
    if c == 0:
        numeroMaior = lista[c]
        numeroMenor = lista[c]
    
    # Se o número digitado for maior
    if lista[c] > numeroMaior:
        numeroMaior = lista[c]
    #Se o número digitado for menor
    elif lista[c] < numeroMenor:
        numeroMenor = lista[c]
    
print('*'*30)



print(f'O maior número inserido foi {numeroMaior} nos índices ', end='')

for i, v in enumerate(lista):
    if v == numeroMaior:
        print(f'{i}...', end='')
        
print()
        
print(f'O menor número inserido foi {numeroMenor} nos índices ', end='')

for i, v in enumerate(lista):
    if v == numeroMenor:
        print(f'{i}...', end='')
        
print()