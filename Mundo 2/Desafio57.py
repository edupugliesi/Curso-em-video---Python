'''
Faça um programa que leia o sexo de uma pessoa, mas só aceita valores 'M' e 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''
sexo = str(input('Digite o sexo: [M/F]')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Valor inválido, insira novamente: ')).upper()
print('Sexo {} registrado!'.format(sexo))
print('Fim')