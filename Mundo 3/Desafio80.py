'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (Sem usar o sort)
No final, mostre a lista ordenada na tela
'''


lista = []
numero = 0

for c in range(0, 5):
    numero = int(input('Insira um número: '))
    
    # Se o número for o primeiro ou o maior da lista
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista!')
    
    # Se o número não for o primeiro e nem o maior da lista
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado a posição {pos} da lista!')
                break
            pos += 1
print()
print(f'Os valores digitados em ordem foram {lista}')
        
    
        
        

