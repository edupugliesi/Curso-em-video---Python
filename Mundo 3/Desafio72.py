'''
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso de ZERO até VINTE.
Se programa deverá ler um número pleo teclado (Entre 0 e 20) e mostra-lo por extenso
'''

numerosPorExtenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
                     'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
                     'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 
                     'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numeros = 0

print(len(numerosPorExtenso))

while True:
    
    numeros = int(input('Insira um número inteiro de 1 até 20: '))
    
    while numeros > 20 or numeros < 1:
        numeros = int(input('Número inválido. Insira um número inteiro de 1 até 20: '))
    
    print(f'O número digitado foi {numerosPorExtenso[numeros - 1]}')
    
    '''if numeros == 1:
        print(f'O número escolhido foi {numerosPorExtenso[0]}')
    elif numeros == 2:
        print(f'O número escolhido foi {numerosPorExtenso[1]}')
    elif numeros == 3:
        print(f'O número escolhido foi {numerosPorExtenso[2]}')
    elif numeros == 4:
        print(f'O número escolhido foi {numerosPorExtenso[3]}')
    elif numeros == 5:
        print(f'O número escolhido foi {numerosPorExtenso[4]}')
    elif numeros == 6:
        print(f'O número escolhido foi {numerosPorExtenso[5]}')
    elif numeros == 7:
        print(f'O número escolhido foi {numerosPorExtenso[6]}')
    elif numeros == 8:
        print(f'O número escolhido foi {numerosPorExtenso[7]}')
    elif numeros == 9:
        print(f'O número escolhido foi {numerosPorExtenso[8]}')
    elif numeros == 10:
        print(f'O número escolhido foi {numerosPorExtenso[9]}')
    elif numeros == 11:
        print(f'O número escolhido foi {numerosPorExtenso[10]}')
    elif numeros == 12:
        print(f'O número escolhido foi {numerosPorExtenso[11]}')
    elif numeros == 13:
        print(f'O número escolhido foi {numerosPorExtenso[12]}')
    elif numeros == 14:
        print(f'O número escolhido foi {numerosPorExtenso[13]}')
    elif numeros == 15:
        print(f'O número escolhido foi {numerosPorExtenso[14]}')
    elif numeros == 16:
        print(f'O número escolhido foi {numerosPorExtenso[15]}')
    elif numeros == 17:
        print(f'O número escolhido foi {numerosPorExtenso[16]}')
    elif numeros == 18:
        print(f'O número escolhido foi {numerosPorExtenso[17]}')
    elif numeros == 19:
        print(f'O número escolhido foi {numerosPorExtenso[18]}')
    elif numeros == 20:
        print(f'O número escolhido foi {numerosPorExtenso[19]}')'''
    
    op = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()
    
    if op != 'S':
        break
    
print('\nFim do programa. Volte sempre!')