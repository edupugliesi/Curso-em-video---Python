
print('-'*30) #Espaçamento

#Printar 1 até 9 com FOR
for c in range(1, 10):
    print(c, end=' ')
print('Fim, com FOR')

print('-'*30) #Espaçamento

#Printar de 1 até 9 com WHILE
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('Fim, com WHILE')

print('-'*30) #Espaçamento

#WHILE com condição de parada
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim, WHILE condição de parada!')

print('-'*30) #Espaçamento

#Fazer média com WHILE
n = 0
s = 0
m = 0
r = 'S'
count = 0

while r == 'S':
    n = int(input('\nDigite uma nota: '))
    
    count += 1
    s += n
    m = s / count
    
    r = str(input('Exitem mais notas? [S/N]: ')).upper()
print('A quantidade de notas foram {} e a média final foi {}'.format(count, m))
    
    




