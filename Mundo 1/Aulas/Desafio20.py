#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem dos alunos para apresentar o trabalho são: {}'.format(lista))