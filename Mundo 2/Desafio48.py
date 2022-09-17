#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
#e que se encontram no intervalo de 1 até 500

s = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        s = c + c


print(s)