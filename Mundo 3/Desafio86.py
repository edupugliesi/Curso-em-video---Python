'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado

No final, mostre a matriz na tela, com a formatação correta.
'''

print('='*30)

matriz = [[], [], []]
numeros = 0

for a in range(0, 3):
    numeros = int(input(f'Digite o {a+1}º da primeira linha: '))
    matriz[0].append(numeros)

for b in range(0, 3):
    numeros = int(input(f'Digite o {b+1}º da segunda linha: '))
    matriz[1].append(numeros)
    
for c in range(0, 3):
    numeros = int(input(f'Digite o {c+1}º da terceira linha: '))
    matriz[2].append(numeros)

print('='*30)
print('A matriz digitada foi: ')
print(matriz[0])
print(matriz[1])
print(matriz[2])
    