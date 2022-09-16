#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "Santo"

nome = str(input('Qual o seu nome? ')).strip()
cidade = str(input('Ola {}, qual cidade você nasceu? '.format(nome)))
validacao = cidade.split()

#print(validacao)

print('O nome da cidade começa com Santo? ', 'Santo' in validacao[0])