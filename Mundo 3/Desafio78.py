'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
'''

numero = 0
numeroMaior = numero 
numeroMenor = numero
lista = []

for c in range(1, 6):
    numero = int(input(f'Digite o {c}º número: '))
    lista.append(numero)
    
    if numero < numeroMenor:
        numeroMenor = numero
        print(numeroMenor)
            
    if numero > numeroMaior:
        numeroMaior = numero
        print(numeroMaior)
    
print('*'*30)
print(numeroMaior)
print(numeroMenor)
print(lista)