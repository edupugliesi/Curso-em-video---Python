#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = str(input('\nQual o seu nome? '))
salario = float(input('Qual o seu salário? '))

aumento = salario * 0.15
salarioFinal = aumento + salario

print('Olá {}, seu salário era R${}, teve R${:.2f} de aumento. Você agora vai receber R${:.2f}'.format(nome, salario, aumento, salarioFinal))
