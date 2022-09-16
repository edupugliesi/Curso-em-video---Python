#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com a sua idade

#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: Sênior
#Acima: Master

from datetime import date

print('='*30)

nome = str(input('Qual o seu nome? '))
anoNascimento = int(input('Ola {}, qual ano você nasceu? '.format(nome)))

idade = date.today().year - anoNascimento

if idade <= 9:
    print('Olá {}, você tem {} anos e participa da categoria Mirim!'.format(nome, idade))
elif idade <= 14:
    print('Ola {}, você tem {} anos e participa da categoria Infantil!'.format(nome, idade))
elif idade <= 19:
    print('Ola {}, você tem {} anos e participa da categoria Junior!'.format(nome, idade))
elif idade <= 25:
    print('Ola {}, você tem {} anos e participa da categoria Sênior!'.format(nome, idade))
elif idade > 25:
    print('Ola {}, você tem {} anos e participa da categoria Master!'.format(nome, idade))