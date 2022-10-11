print('='*100)

pessoa = {} # Declaração do dicionário

# Inserindo dados no dicionário
pessoa['Nome'] = 'Eduardo'
pessoa['Idade'] = 26
pessoa['Sexo'] = 'M'
pessoa['Peso'] = 98

# Printando o dicionário
print(pessoa)

# Deletando elementos do dicionário
del pessoa['Peso']

print(pessoa) # Printando o dicionário Pessoa

print('='*100)

# Declarando dicionário com dados
filme = {
    'Titulo': 'Star Wars',
    'Ano': 1977,
    'Diretor': 'George Lucas'
}
filme2 = {
    'Titulo': 'Avenger',
    'Ano': 2010,
    'Diretor': 'Joss Whedom'
}
filme3 = {
    'Titulo': 'Matrix',
    'Ano': 1999,
    'Diretor': 'Wachowski'
}


print(filme)
print(filme.values()) # Printando apenas os valores do dicionário
print(filme.keys()) # Printando apenas os índices do dicionário
print(filme.items()) # Printando o dicionário separado por itens

# Printando o dicionário formatado
for k, v in filme.items():
    print(f'O {k} é {v}')
    
print('='*100)

# Declarando uma lista Locadora
locadora = []

locadora.append(filme) # Inserindo o dicionário Filme dentro da Lista.
locadora.append(filme2) # Inserindo o dicionário Filme2 dentro da Lista.
locadora.append(filme3) # Inserindo o dicionário Filme3 dentro da Lista.

print(locadora)

print(locadora[0]['Ano']) # Printando o ANO do filme 0 da lista locadora.
print(locadora[2]['Titulo']) # Printando o Titulo do filme 2 da lista locadora


print('='*100)

estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Siga do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}. ', end='')
    print()

print(brasil)
