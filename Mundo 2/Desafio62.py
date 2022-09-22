'''
Melhore o Desafio61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encessa quando ele dizer que quer mostrar 0 termos.
'''

print('-=-'*10)

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = primeiroTermo 
count = 1
totalTermos = 0
maisTermos = 10

while maisTermos != 0:
    totalTermos = totalTermos + maisTermos
    
    while count <= totalTermos:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        count = count + 1
    
    print('Pausa')
    maisTermos = int(input('Deseja exibir mais quantos termos? '))
    print('-'*30)
    
print('Finalizado com {} termos!'.format(totalTermos))