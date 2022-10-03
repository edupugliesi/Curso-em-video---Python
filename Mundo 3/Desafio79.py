'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista la dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
em ordem crescente.
'''

lista = []
count = 1

while True:
    numeros = int(input(f'Insira o {count}º número: '))
    count += 1
    
    # Verificar se o número digitado já existe na lista
    while numeros in lista:
        numeros = int(input('Número já existe na lista, insira outro valor: '))
    
    lista.append(numeros)
    
   
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    
    print('-'*30)
        
    if op != 'S':
        break

lista.sort()
print(f'Números inseridos em ordem crescente são: {lista}')