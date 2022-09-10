#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

nome = str(input('Qual o seu nome? '))
metro = float(input('Insira o valor em metros: '))

cm = metro*100
mm = metro*1000

print('Olá {} \n{} metro(s) é igual a {} centímetros \n{} metro(s) é igual a {} milímetros'.format(nome, metro, cm, metro, mm))