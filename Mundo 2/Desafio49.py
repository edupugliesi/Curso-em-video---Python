'''Refaça o desafio9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando FOR'''

print('+'*30)
print('Vamos fazer uma tabuada!')
n = float(input('Digite um número: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n * c))
print('FIM')