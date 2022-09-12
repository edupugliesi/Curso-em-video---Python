#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

nome = str(input('Qual o seu nome? '))
angulo = float(input('Insira um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print('Olá {}, o Ângulo {} possui: \nseno: {:.2f} \ncosseno {:.2f} \ntangente {:.2f}'.format(nome, angulo, seno, cosseno, tangente))
