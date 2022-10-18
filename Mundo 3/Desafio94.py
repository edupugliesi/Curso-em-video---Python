'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:

A - Quantas pessoas foram cadastradas.
B - A média de idade do grupo
C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média

'''
print('='*30)

pessoa = {}
grupo = []
mulheres = []
idadeAcima = []
somaIdade = mediaIdade = 0

count = 1

while True:
    print(f'\n-- {count}º pessoa --\n')
    # Input nome e sexo no dicionário
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo: ')).upper().strip()
    
    # Validar se o sexo foi digitado com a opção correta M ou F
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo inválido, insira M ou F: ')).upper().strip()
    
    # Input idade no dicionário
    pessoa['idade'] = int(input('Idade: '))
    
    # Somar todas as idades inseridas no dicionário pessoa
    somaIdade += pessoa['idade']
    
    # Adicionando o dicionário pessoa na lista grupo
    grupo.append(pessoa.copy())
    
    # Limpar dicionário pessoa para receber uma nova pessoa
    pessoa.clear()
    
    # Operação para encerrar o programa com validação de opção S ou N.
    op = str(input('Deseja continuar? [S/N]: ' )).strip().upper()
    while op not in 'NS':
        op = str(input('Opção inválida, digite S ou N: ' )).strip().upper()
        
    if op == 'N':
        print('='*30)
        break
    
    count += 1 # Contador
    print('-'*30)


# Printar quantas pessoas foram cadastradas
print(f'Foram cadastrados {len(grupo)} pessoas')

# Média de idade do grupo
print(f'A média de idade do grupo é {somaIdade / len(grupo)}')

# Quais as mulheres do grupo
print(f'As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

# Pessoas com idade maior que a média do grupo
print(f'As pessoas com idade maior que a média do grupo de {somaIdade / len(grupo)} anos são: ', end='')
for p in grupo:
    if p['idade'] > (somaIdade / len(grupo)):
        print(f'{p["nome"]} ', end='')
print()
print('Fim!')





        