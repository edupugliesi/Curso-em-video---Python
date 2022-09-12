#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânculo, calcule e mostre
#o comprimento da hipotenusa

from math import sqrt

nome = str(input('\nQual o seu nome? '))
catetoOposto = float(input('Digite o Cateto Oposto: '))
catetoAdjacente = float(input('Digite o Cateto Adjacente: '))

hipotenusa = (catetoOposto**2) + (catetoAdjacente**2)

print('Olá {},\nO Cateto Oposto é {} \nO Cateto Adjacente é {} \nPortanto a hipotenusa é {}'.format(nome, catetoOposto, catetoAdjacente, hipotenusa**(1/2)))

#Utilizando a biblioteca Math
print('Olá {},\nO Cateto Oposto é {} \nO Cateto Adjacente é {} \nPortanto a hipotenusa é {}'.format(nome, catetoOposto, catetoAdjacente, sqrt(hipotenusa)))
