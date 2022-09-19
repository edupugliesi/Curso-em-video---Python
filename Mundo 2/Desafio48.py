#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
#e que se encontram no intervalo de 1 até 500

print('-'*30)

s = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        cont += 1


print('A soma de todos os {} valores informados é: {}'.format(cont, s))