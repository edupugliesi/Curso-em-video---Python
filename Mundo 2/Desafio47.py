#Crie um programa que mostre na tela todos os números PARES que estão no intervalo entre 1 e 50.
print('-'*30)
print('Primeira Forma!')

for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        
print('-'*30)
print('Segunda Forma')

for c in range(0, 51, 2):
    print(c)
    