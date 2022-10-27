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

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor
    
    

texto('Validar dados')
n = leiaint('Digite um número: ')

print(f'Você acabou de digitar o número {n}')
