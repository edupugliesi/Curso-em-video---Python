#Desenvolva um programa que pergunta a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
#E R$0,45 para viagens mais longas

nome = str(input('Qual o seu nome? '))
distancia = float(input('Qual a distâcia da sua viagem? '))

if distancia >= 200:
    preço = distancia * 0.45
    print('{} sua viagem é maior que 200km, o preço da sua passagem será R${:.2f}'.format(nome, preço))
if distancia < 200:
    preço = distancia * 0.50
    print('{} sua viagem será menor que 200km, o preço da sua passagem será R${:.2f}'.format(nome, preço))
