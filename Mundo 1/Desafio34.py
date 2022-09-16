#Escreva um programa que pergunte o salário do funcionário e calcule o valor de seu aumento
#Para salários superiores a R$1250,00, calcule um aumento de 10%
#Para inferiores ou iguais a R$1250,00, o aumento é de 15%.

nome = str(input('Qual o seu nome? '))
salario = float(input('Qual o seu salário? '))

if salario > 1250:
    salarioNovo = (salario / 10) + salario
    print('{} você recebeu um aumentode 10%, seu salário era R${:.2f} e agora será R${:.2f}'.format(nome, salario, salarioNovo))
if salario <= 1250:
    salarioNovo = (salario / 15) + salario
    print('{} você recebeu um aumentode 15%, seu salário era R${:.2f} e agora será R${:.2f}'.format(nome, salario, salarioNovo))