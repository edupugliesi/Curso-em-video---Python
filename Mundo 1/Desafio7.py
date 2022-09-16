#Desenvolva um programa que leia as duas notas de um aluno, calcle e mostre a sua média

nome = str(input('Qual o seu nome?\n'))
nota1 = float(input('Qual a sua primeira nota?\n'))
nota2 = float(input('Qual a sua segunda nota?\n'))

media = (nota1 + nota2)/2

print('Olá {},\nSua primeira nota foi {}\nSua segunda nota foi {}\nSua média é {}'.format(nome, nota1, nota2, media))