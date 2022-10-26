'''
Crie uma função que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular, e outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial
'''

def texto(msg):
    linha = len(msg) + 4
    print()
    print('-' * linha)
    print(f'  {msg}')
    print('-' * linha)
    print()

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    texto(f'O fatorial de {num} é igual a {f}')


def calculo(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        print(f)
    
    

texto('Fatorial')
n = (int(input('Digite um número: ')))
fatorial(n)

op = str(input('Deseja mostrar todo o calculo? [S/N] ')).upper().strip()
if op == 'S':
    calculo(n)
else:
    texto('Fim')


