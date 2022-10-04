"""test = []
test.append('Eduardo')
test.append(26)

galera = []
galera.append(test[:])

test[0] = 'Roberval'
test[1] = 64

galera.append(test[:])
print(galera)"""

###################################################################################################

'''galera = [['Eduardo', 26], ['Vanderson', 47], ['Paula', 51], ['Manuela', 18]]
print(galera)
print(galera[2][1]) # Print idade Paula

# Printar todas as pessoas
for pessoa in galera:
    print(pessoa[0])

# Printar todas as idades
for idade in galera:
    print(idade[1]) 
    
# Printar pessoa e idade
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')'''
    
    
###################################################################################################

galera = []
dado = []
totalMaior = totalMenor = 0
termoCorretoMaior = ''
termoCorretoMenor = ''

# For para inserção de 3 pessoas na lista
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Gerar uma cópia da lista dado para a lista galera
    dado.clear() # Apaga a lista dado
    print('*'*20)
    
print('\nGalera: ', galera, '\n')

# For para descobrir quantas e quais pessoas da lista GALERA são maiores ou menores de idade
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade!')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        totalMenor += 1
    print('-'*20)
    
# IF para printar o termo "menor" no plural ou singular
if totalMenor == 1:
    termoCorretoMenor = 'menor'
else:
    termoCorretoMenor = 'menores'
    
# IF para printar o termo "maior" no plugar ou singular
if totalMaior == 1:
    termoCorretoMaior = 'maior'
else:
    termoCorretoMaior = 'maiores'
        
        
print(f'A lista tem {totalMaior} {termoCorretoMaior} de idade e {totalMenor} {termoCorretoMenor} de idade')