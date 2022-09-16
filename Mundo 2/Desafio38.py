#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais.

nome = str(input('Qual o seu nome? '))
print('==- {} VAMOS JOGAR UM JOGO, VOCÊ VAI INSERIR 2 NUMEROS INTEIROS E EU OS ANALISAREI!'.format(nome.upper()))
n1 = int(input('Número 1: '))
n2 = int(input('Numero 2: '))

if n1 > n2:
    print('{}, {} é maior que {}!'.format(nome, n1, n2))
elif n2 > n1:
    print('{}, {} é maior que {}!'.format(nome, n2, n1))
elif n1 == n2:
    print('{}, {} e {} são iguais'.format(nome, n1, n2))
    

