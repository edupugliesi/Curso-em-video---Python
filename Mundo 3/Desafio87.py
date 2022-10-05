'''
Aprimore o desafio anterior mostrando no final:
A - A soma de todos os valores pares digitados
B - A soma de todos os valores da terceira coluna.
C - O maior valor da segunda linha
'''

print('='*30)

matriz = [[], [], []]
somaPar = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0
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
print(somaPar)
print('A matriz digitada foi: ')
print(matriz[0])
print(matriz[1])
print(matriz[2])
