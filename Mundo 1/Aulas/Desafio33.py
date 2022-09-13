#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

nome = str(input('Qual o seu nome? '))
print('Informe três números e lhe darei sua ordem decrescente')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

if n1 > n2 and n2 > n3:
    print('Os números em ordem são: {}, {} e {}'.format(n1, n2, n3))
if n3 > n2 and n2 > n1:
    print('Os números em ordem são: {}, {} e {}'.format(n3, n2, n1))
if n2 > n1 and n1 > n3:
    print('Os números em ordem são: {}, {} e {}'.format(n2, n1, n3))
if n3 > n1 and n1> n2:
    print('Os números em ordem são: {}, {} e {}'.format(n3, n1, n2))
if n1 > n3 and n3 > n2:
    print('Os números em ordem são: {}, {} e {}'.format(n1, n3, n2))
if n2 > n3 and n3 > n1:
    print('Os números em ordem são: {}, {} e {}'.format(n2, n3, n1))