#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

#1 - Para binário
#2 - Para Octal
#3 - Para Hexadecimal

print('-'*30)


numero = int(input('Digite um número inteiro: \n'))
print('''Escolha uma das bases para conversão:
      [1] Converter para binário
      [2] Converter para octal
      [3] Converter para hexadecimal''')

op = int(input('\nInsira a opção desejada: '))

if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Insira uma opção válida!')