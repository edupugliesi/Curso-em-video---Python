nome = input('Qual seu nome? ')
algo = input('Insira algo: ')

print('{} "{}" é um número? {}'.format(nome, algo, algo.isnumeric()))
print('{} "{}" é um letra? {}'.format(nome, algo, algo.isalpha()))
print('{} "{}" é um alphanumérico? {}'.format(nome, algo, algo.isalnum()))
print('{} "{}" é está todo em maíusculo? {}'.format(nome, algo, algo.isupper()))
print('{} "{}" é está todo me minúsculo? {}'.format(nome, algo, algo.islower()))