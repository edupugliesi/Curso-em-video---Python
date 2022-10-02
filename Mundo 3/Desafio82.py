'''
Crie um programa que vai ser vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente
Ao final, mostre o conteúdo das três listas geradas
'''

numero = 1
lista = []
listaPar = []
listaImpar = []
op = ''
count = 1

while True:
    numero = int(input(f'Digite o {count}º número: '))
    
    while numero <= 0:
        numero = int(input('Número Inválido. Digite um número inteiro e maior que 0: ' ))
        
    count += 1
    lista.append(numero)
    
    if numero % 2 == 0:
        listaPar.append(numero)
    elif numero % 2 != 0:
        listaImpar.append(numero)
    
    
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    
    print('-'*30)
    
    if op != 'S':
        break

print(f'Os números inseridos foram: {lista}')
print(f'Os números pares inseridos foram: {listaPar}')
print(f'Os números ímpares inseridos foram: {listaImpar} ')