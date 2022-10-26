'''
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas valor numérico
'''

def texto(msg):
    linha = len(msg) + 4
    print()
    print('-' * linha)
    print(f'  {msg}')
    print('-' * linha)
    print()

def leiaint(n):
    n = input('Insira um número: ')
    
    while n != int or n != float:
        n = input('Valor inválido, por favor informe um número: ')
    print(f'O valor digitado foi o número {n}')

texto('Validar dados')
leiaint(5)
