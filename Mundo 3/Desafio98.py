'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
Seu programa tem que realizar três contagens através da função criada

A - De 1 até 10, de 1 em 1
B - De 10 até 0, de 2 em 2
C - Uma contagem personalizada
'''

def mensagem(msg):
    print()
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))
    print()

def contador():
    mensagem('A - Contanto 1 até 10, de 1 em 1')
    for c in range(1, 11):
        print(f'{c} ', end='')
    print()
        
    mensagem('B - Contado de 10 até 0, de 2 em 2')
    for c in range(10, -1, -2):
        print(f'{c} ', end='')
    print()
        
    mensagem('Contagem personalizada')
    inicio = int(input('Digite o ínicio da contagem: '))
    fim = int(input('Digite o final da contagem: '))
    passo = int(input('Digite o passo da contagem: '))
    
    if inicio < fim:
        mensagem('Contagem progressiva: ')
        while inicio != fim:
            inicio += passo
            print(f'{inicio} ', end='')
        print()
            
    elif inicio > fim:
        mensagem('Contagem regressiva: ')
        while inicio != fim:
            inicio -= passo
            print(f'{inicio} ', end='')
        print()

contador()