#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas
#Nome com todas as letra minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome completo? '))

print('Seu nome com todas as letras maiúsculas: {} '.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {} '.format(nome.lower()))

nomeSemEspaços = nome.replace(' ', '')

print('Seu nome possui {} letras em contar os espaços'.format(len(nomeSemEspaços)))

primeiroNome = nome.split()

print('Seu primeiro nome possui {} letras'.format(len(primeiroNome[0])))