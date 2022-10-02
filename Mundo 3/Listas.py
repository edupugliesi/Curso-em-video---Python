

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

print(lanche)

lanche.append('rosquinha') # Adiciona um novo elemento ao final da lista.

print(lanche)

lanche.insert(0, 'cachorro quente') # Adiciona um elemento na posição desejada.

print(lanche)

#del lanche[3] # Deleta o elemento desejado da lista pelo índice
#lanche.pop(3) # Deleta o elemento desejado da lista pelo índice. Sem valor de referência para remover o último elemento.
lanche.remove('pizza') # Deleta elemento da lista pelo valor.

print(lanche)

valores = [8, 2, 5, 4, 9, 3, 0]

print(valores)

valores.sort() # Ordenar a lista em ordem crescente

print(valores)

valores.sort(reverse=True) # Ordenara a lista em ordem DEcrescente

print(valores)
print(len(valores)) # Mostra quantos elementos existem na lista

valores2 = []
for cont in range(0, 5):
    valores2.append(int(input('Insira um valor: '))) # Inserindo valores em uma lista através de um INPUT

for c, v in enumerate(valores2):
    print(f'Na posição {c} encontrei o valor {v}!') # Mostrando os valores formatados de uma lista através de um FOR
    
valores3 = valores2[:] # Criando uma cópia da Lista VALORES2 em VALORES3, sem criar uma ligação entre elas.

print(valores3)
print('Fim!')