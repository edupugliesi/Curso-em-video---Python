'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços

Ex: APOS A SOPA
A SACADA DA CASA
A TORRE DA DETTORA
O LOBO AMA BOLO
ANOTARAM A DATA DA MARATONA
'''

frase = str(input('Digite uma frase: ')).strip().upper()
fraseJunta = frase.replace(' ', '')
fraseInversa = ''

for letra in range(len(fraseJunta) -1, -1, -1):
    fraseInversa += fraseJunta[letra]

print(fraseJunta)
print(fraseInversa)

if fraseJunta == fraseInversa:
    print('A frase é um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')