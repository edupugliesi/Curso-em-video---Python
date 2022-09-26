#Declarando uma TUPLA com ().
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #Tuplas são imutáveis
print(lanche[1], lanche[3]) #Printando elementos 1 e 3 da Tupla (Suco e Pudim)

print(lanche[1:3]) #Printando elementos 1 e 2, desconsiderando o 3º. (Suco, Pizza)
print(lanche[:2]) #Printando elementos 0 e 1 da Tupla, desconsiderando o 2º (Hamburguer, suco)
print(sorted(lanche))

print('-'*30)

#Printar todas as comidas com FOR IN
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Estou de bucho cheio! FOR IR\n')

#Printar todas as comidas com FOR RANGE
for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')
print('Estou de bucho cheio! FOR RANGE\n')

#Printar todas as comidas com For ENUMERATE
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Estou com bucho cheio! FOR ENUMERATE\n')

print('-'*30)

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b

print(c) #Printa a concatenação das Tuplas A e B
print(len(c)) #Mostra quantos elementos tem a Tupla C
print(c.count(5)) #Mostra quantas vezes aparece o número 5 na Tupla C
print(c.index(4)) #Mostra em qual posição está o número 4

print('-'*30)

pessoa = ('Eduardo', 26, 'M', 100) #Tupla com tipos de dados diferentes
print(pessoa)
del(pessoa) #Deletar uma Tupla

"""soma = []

while True:
    soma = a[0] + b[0]
    a += [1]
    b += [1]
    
    break
print(soma)
"""