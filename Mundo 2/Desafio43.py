#Desenvolva uma lógica que leia o peso e a altura de uma pessoa
#Calcule seu IMc e mostre seu status, de acordo com a tabela abaixo.

#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida.

print('-'*30)

nome = str(input('Qual o seu nome? '))
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura**2)

#print (imc)

if imc <= 18.5:
    print('Olá {}, seu IMC é {:.2f}, você está ABAIXO DO PESO!'.format(nome, imc))
elif imc <= 25:
    print('Olá {}, seu IMC é {:.2f}, você está em seu PESO IDEAL!'.format(nome, imc)) 
elif imc <= 30:
    print('Olá {}, seu IMC é {:.2f}, você está em SOBREPESO!'.format(nome, imc))
elif imc <= 40:
    print('Olá {}, seu IMC é {:.2f}, você está OBESO!'.format(nome, imc))
elif imc > 40:
    print('Olá {}, seu IMC é {:.2f}, você está em OBESIDADE MÓRBIDA!'.format(nome, imc))