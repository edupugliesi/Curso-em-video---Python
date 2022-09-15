#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade

#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou o tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
print('=' * 30)
nome = str(input('Qual o seu nome? '))
idade = int(input('{}, qual a sua idade? '.format(nome)))

if idade == 18:
    print('{}, você tem {} anos. Está na hora de se alistar ao serviço militar obrigatório!'.format(nome, idade))
elif idade > 18:
    print('{}, você tem {} anos e se alistou ao serviço militar obrigatório há {} anos atrás'.format(nome, idade, idade - 18))
elif idade < 18:
    print('{}, você tem {} anos. Ainda faltam {} anos para você se alistar ao serviço militar obrigatório!'.format(nome, idade, 18 - idade))


