'''
Faça um programa que leia o sexo de uma pessoa, mas só aceita valores 'M' e 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''
sexo = str(input('Digite o sexo: ')).upper()
while sexo != 'F' or sexo != 'M':
    sexo = str(input('Valor inválido, insira novamente: ')).upper()
    print(sexo)
print('Fim')