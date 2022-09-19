'''
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre:

A media de idade do grupo,
Qual o nome do homem mais velho,
Quantas mulheres tem menos de 21 anos,

'''

MediaIdade = 0
IdadeTotal = 0

MaiorIdade = 0
count = 0
NomeHomemMaiorIdade = ''

for c in range(1, 5):
    print('\n--- {}º PESSOA ---\n'.format(c))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()
    
    IdadeTotal =+ idade
    MediaIdade = IdadeTotal / c
    
    if sexo == 'M':
        MaiorIdade = idade
        NomeHomemMaiorIdade = nome
    if sexo == 'F' and idade < 21:
        count += 1
    
print('\nA média de idade do grupo é {} anos!'.format(MediaIdade))
print('Existem {} mulheres com menos de 21 anos!'.format(count))
print('O homem com a maior idade tem {} e se chama {}'.format(MaiorIdade, NomeHomemMaiorIdade))
