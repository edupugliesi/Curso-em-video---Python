#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

#Ex: Ana Maria de Souza
#Primeiro: Ana
#Ultimo: Souza

nome = str(input('Qual o seu nome completo? ')).strip()
nome = nome.split()

print('Seu primeiro nome é {} e seu último nome é {}'.format(nome[0], nome[len(nome) -1 ]))