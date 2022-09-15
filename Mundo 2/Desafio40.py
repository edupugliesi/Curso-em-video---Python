#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média acima de 7.0 ou superior: Aprovado

print('=' * 30)

nome = str(input('Qual o seu nome? '))
n1 = float(input('Qual a nota da primeira prova? '))
n2 = float(input('Qual a nota da segunda prova? '))
media = (n1 + n2) / 2

if media < 5:
    print('{}, sua média foi {} e você está reprovado!'.format(nome, media))
elif media >= 5 and media <= 6.9:
    print('{}, sua média foi {} e você está de recuperação!'.format(nome, media))
elif media >= 7:
    print('Parabéns {}, sua média foi {} e você está APROVADO!'.format(nome, media))
    
    