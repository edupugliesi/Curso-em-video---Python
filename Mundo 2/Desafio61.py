'''
Refaça o Desafio51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da prograssão
usando a estrutura WHILE
'''

print('-=-'*10)

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
termo = primeiroTermo 
count = 1

while count <= 10:
    print('{} > '.format(termo), end='')
    termo = termo + razao
    count = count + 1
print('Fim')
    