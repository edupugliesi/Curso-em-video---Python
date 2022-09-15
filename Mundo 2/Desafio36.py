#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salaŕio ou então o empréstimo será negado

nome = str(input('Qual o seu nome? '))
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quer financiar em quantos anos? '))
meses = anos * 12
parcelas = casa / meses

parcelaMaxima = salario * 30 / 100

if parcelas > parcelaMaxima:
    print('{}, o valor da parcela supera em 30% do seu salário. Financiamento negado!'.format(nome))
elif parcelas <= parcelaMaxima:
    print('{} financiamento aprovado! Você pagará R${:.2f} por mês durante {} meses'.format(nome, parcelas, meses))