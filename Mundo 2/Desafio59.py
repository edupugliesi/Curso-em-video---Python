'''
Crie um programa que leia dois valores e mostre um menu na tela

1 - Somar
2 - Multiplicar
3 - Maior que
4 - novos numeros
5 - sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0

while op != 5:
    print('''
    Selecione uma opção!

    1 - SOMA
    2 - MULTIPLICAÇÃO
    3 - MAIOR QUE
    4 - NOVOS NÚMEROS
    5 - SAIR DO PROGRAMA
    ''')

    op = int(input('Selecione uma opção: '))
    
    if op == 1:
        print('\nA soma de {} + {} é {}!'.format(n1, n2, n1+n2))
    elif op == 2:
        print('\nA multiplicação de {} x {} é {}!'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('\n{} é maior que {}!'.format(n1, n2))
        elif n2 > n1:
            print('\n{} é maior que {}!'.format(n2, n1))
        elif n1 == n2:
            print('\n{} e {} são iguais!'.format(n1, n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))
    elif op >= 6:
        print('\nOpção inválida, tente novamente!')
        
print('Fim')



