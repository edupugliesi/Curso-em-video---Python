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

# Inserir números na primeira linha
for a in range(0, 3):
    numeros = int(input(f'Digite o {a+1}º da primeira linha: '))
    matriz[0].append(numeros)
    # Somar elementos da primeira linha
    if numeros % 2 == 0:
        somaPar += numeros
    

# Inserir números na segunda linha
for b in range(0, 3):
    numeros = int(input(f'Digite o {b+1}º da segunda linha: '))
    matriz[1].append(numeros)
    # Somar elementos da segunda linha com a soma dos elementos da primeira linha
    if numeros % 2 == 0:
        somaPar += numeros

# Inserir números na terceira linha
for c in range(0, 3):
    numeros = int(input(f'Digite o {c+1}º da terceira linha: '))
    matriz[2].append(numeros)
    # Somar elementos da terceira linha com a soma dos elementos das linhas anteriores.
    if numeros % 2 == 0:
        somaPar += numeros
        
# Somar elementos da terceira coluna
somaTerceiraColuna = matriz[0][2] + matriz[1][2] + matriz [2][2]

# Descobrir o elemento maior da segunda linha
for c in range(0, 3):
    if c == 0:
        maiorSegundaLinha = matriz[1][c]
    elif matriz[1][c] > maiorSegundaLinha:
        maiorSegundaLinha = matriz[1][c]
    
    

    
    
print('='*30)
print(somaPar)
print('A matriz digitada foi: ')
print(f'  {matriz[0]}  ')
print(f'  {matriz[1]}  ')
print(f'  {matriz[2]}  ')

print(f'A soma dos números pares é: {somaPar}')
print(f'A soma dos números da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior numero da segunda coluna é: {maiorSegundaLinha}')
