#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor!

nome = input('Qual seu nome? ')
n = int(input('Insira um número: '))

print('Olá {} o número digitado foi {}. Seu antecessor é {} e seu sucessor é {}'.format(nome.upper(), n, n-1, n+1))