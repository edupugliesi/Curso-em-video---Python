# Função sem parâmetro
def linha():
    print('-'*30)

# Função com parâmetro
def mensagem(msg):
    print('-'*10)
    print(msg)
    print('-'*10)
    
# Função de soma
def soma(a, b):
    print(f'A = {a} / B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

# Função para dobrar os valores de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

# Função para somar vários números
def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(s)


# Print usando função sem parâmetro
linha()
print('            ALUNOS            ')
linha()
linha()
print('            NOTAS            ')
linha()

# Print usando função com parâmetro
mensagem('ALUNOS')
mensagem('NOTAS')

mensagem('Soma')
soma(4.5, 5.4)

mensagem('Outra soma')
soma(3.75, 9.87)

mensagem('Soma com INPUT')
soma(float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: ')))

mensagem('Dobrando uma lista')
lista = [2, 4, 6, 8, 10]
dobra(lista)

mensagem('Soma de diversos valores')
soma2(3, 4, 5)
soma2(3, 2, 9, 7, 0)
soma2(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)



