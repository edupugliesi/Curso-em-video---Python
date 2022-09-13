nome = str(input('Qual é o seu nome? '))

if nome == 'Eduardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('{} a sua média foi: {}!'.format(nome, m))

if m >= 6:
    print('{} você está aprovado!'.format(nome))
else:
    print('{} você está reprovado, estude mais.'.format(nome))
    
#Forma simplificada
print('Parabéns' if m >= 6 else 'Estude mais burrão')

