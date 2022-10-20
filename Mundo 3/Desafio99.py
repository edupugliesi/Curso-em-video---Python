'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
Seu programa tem que analisar todos os valores e dizer qual deles é maior.
'''

def mensagem(msg):
    print()
    print('#'*len(msg))
    print(msg)
    print('#'*len(msg))
    print()
    
def maior():
    count = 1
    numMaior = numero = 1
    while numero != 0:
        numero = int(input(f'Insira o {count}º número inteiro (Digite 0 para parar): '))
        
        if count == 1:
            numMaior = numero
        elif numero > numMaior:
            numMaior = numero
            
        
        
        if count == 1 and numero == 0:
            mensagem('Você não inseriu nenhum número!')
            break
        elif count > 1 and numero == 0:
            mensagem(f'O maior número inserido foi {numMaior}')
            break
        
        count += 1

maior()