#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

nome = str(input('Qual seu nome? '))
n = float(input('Insira um número: '))

dobro = n*2
triplo = n*3
rq = n**(1/2)

print('Olá {}, o número digitado foi {} \nSeu dobro é {} \nSeu Triplo é {} \nSua raiz quadrada é {}'.format(nome, n, dobro, triplo, rq))