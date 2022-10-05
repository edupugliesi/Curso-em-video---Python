'''
CRie um programa onde o usuário possa digitar sete valores numeros e cadastre-os em uma lista única
que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente
'''
print('='*30)

numero = 0
numeros = [[], []]


for c in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    elif numero % 2 != 0:
        numeros[1].append(numero)

print('='*30)
print(f'Os números digitados são: {numeros}')
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')