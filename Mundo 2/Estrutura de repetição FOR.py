print('='*20)

#Contar regressivamente até de N até 0
n = int(input('Digite um número alvo: '))

for d in range(n, 0-1, -1):
    print(d, end=' ')
print('Fim contagem regressiva.')

print('-'*20)
#Contar progressivamente de 0 até N

for c in range(0, n+1):
    print(c, end=' ')
(print('Fim contagem progressiva'))

print('-'*20)
#Contar progressivamente de I até F com intervalo P

i = int(input('Digite o início da contagem: '))
f = int(input('Digite fim da contagem: '))
p = int(input('Digite o intervalo da contagem: '))

for b in range(i, f+1, p):
    print(b, end=' ')
print('Fim da contagem de I até F com intervalo P')

s = 0
for a in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(s)
    