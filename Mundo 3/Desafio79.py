'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista la dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
em ordem crescente.
'''

lista = []
numero = 0
count = 1
op = ''

while True:
    numero = int(input(f'Insira o {count}º número: '))
    lista.append(numero)
        
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    count += 1
    
    print('-'*30)
    
        
    if op != 'S':
        break

lista.sort()
print(lista)