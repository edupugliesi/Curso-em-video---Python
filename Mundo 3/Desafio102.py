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

def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)
    
    

texto('Fatorial')

n = int(input('Digite um número: '))

op = str(input('Deseja mostrar todo o calculo? [S/N] ')).upper().strip()
if op == 'S':
    fatorial(n, show=True)

else:
    fatorial(n)




