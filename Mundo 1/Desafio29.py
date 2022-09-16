#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada KM acima do limite

nome = str(input('\nQual o seu nome? '))

velocidade = float(input('{}, qual a velocidade do seu carro? '.format(nome)))

if velocidade <= 80:
    print('Parabéns {}, você está trafegando dentro da velocidade permitida.'.format(nome))
if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 7
    #print(excedente, 'R${}'.format(multa))
    print('{}, você está trafegando acima da velocidade permitida. Você recebeu uma multa de R${:.2f}\n'.format(nome, multa))