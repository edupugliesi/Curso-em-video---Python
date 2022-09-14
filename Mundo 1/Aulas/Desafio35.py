#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

nome = str(input('Qual o seu nome? '))
print('Vamos jogar um jogo. \nInforme o comprimento de 3 retas diferentes e eu informarei se com essas retas podemos formar um triângulo')

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

#print(reta1, reta2, reta3)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('{}, as retas que você inseriu PODEM formar um triângulo!'.format(nome))
else:
    print('{}, as retas que você inseriu NÃO PODEM formar um triângulo!'.format(nome))