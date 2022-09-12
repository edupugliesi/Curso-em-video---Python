#Faça um programa que leia uma frase pelo teclado e mostre

#Quantas vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()
print(frase)
ultimoA = frase.find('a')

print('A sua frase aparece a letra A {} vezes. \nA primeira vez é na posição {} \nA ultima vez na posição {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))