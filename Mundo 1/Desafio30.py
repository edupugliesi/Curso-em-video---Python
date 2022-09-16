#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

nome = str(input('\nQual o seu lindo nome? '))
n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('O número é PAR\n')
if n % 2 != 0:
    print('O número é IMPAR\n')