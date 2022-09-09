##Desafio 3

nome = input('Qual é seu nome? ')

print('Olá', nome, 'vamos fazer uma conta de adição')

n1 = float(input('Digite um número: '))
n2 = float(input('Agora digite outro número: '))

#Print comúm
print(nome, 'a soma entre', n1, 'e', n2, 'é:', n1 + n2)

#Print com métodos
print('{} a soma entre {} e {} é: {} '.format(nome, n1, n2, n1 + n2))