n = 0
s = 0

#Interrompendo uma estrutura While com break.
#Somando todos os elementos de entrada, porém ignorando o ponto de parada 999 sem gambiarras.
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    
#print('A soma vale {}'.format(s))

#Print utilizando F Strings, versão 3.6+
print(f'A soma vale {s}.')