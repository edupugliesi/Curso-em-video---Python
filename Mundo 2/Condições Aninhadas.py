nome = str(input('Qual é o seu nome? '))

if nome == 'Eduardo':
    print('Que nome bonito {}!'.format(nome))
elif nome == 'Joao' or nome == 'Maria':
    print('{} seu nome é bem popular!'.format(nome))
elif nome in 'Ana Claudia Jessia Juliana':
    print('{} que belo nome feminino!'.format(nome))
else:
    print('Poxa {} que nome comúm!'.format(nome))
    
print('Tenha um bom dia {}'.format(nome))