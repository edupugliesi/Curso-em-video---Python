def divisoria(msg):
    print()
    print('#'*len(msg))
    print(msg)
    print('#'*len(msg))
    print()

divisoria('Contador')

def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra o resultado na tela:
        Primeiro parâmetro: Início da contagem
        Segundo parâmetro: Fim da contagem
        Terceiro parâmetro: Passo da contagem
        
    Contagens progressivas e regressivas disponíveis.
    '''
    
    if p == 0 or p < 0:
        print('Insira um PASSO válido.')
    
    elif i == f:
        print('Início e fim são iguais, contagem inválida')
    
    elif i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            c += p
        print('Fim')

    elif i > f:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            c -= p
        print('Fim')
        
        
contador(3, 30, 3)
contador(30, 3, 3)
contador(5, 5, 1)
contador(1, 10, -1)
contador(5, 20, 0)
#help(contador)

divisoria('Fatorial')

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1} {f2} {f3}')

divisoria('Função com RETURN lógico')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print(f'{num} é par')
else:
    print(f'{num} é impar')