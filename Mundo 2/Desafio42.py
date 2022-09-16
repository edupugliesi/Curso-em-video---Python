#Refaça o desafio 035 dos triângulos, acrescentando o recusro de mostrar que tipo de triângulo será formado

#Equilátero: todos os lados são iguais.
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

print('-'*30)

nome = str(input('Qual o seu nome? '))
print('Vamos jogar um jogo. \nInforme o comprimento de 3 retas diferentes e eu informarei se com essas retas podemos formar um triângulo')

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))


#Usando IF's dentro de IF's.

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('{}, as retas que você inseriu PODEM formar um triângulo! '.format(nome), end='')
    if reta1 == reta2 and reta2 == reta3:
        print('Triângulo Equilátero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Triângulo Isóceles!')
    elif reta1 != reta2 and reta2 != reta3:
        print('Triângulo Escaleno!')
else:
    print('{}, as retas que você inseriu NÃO PODEM formar um triângulo!'.format(nome))



#Sem usar IF's dentro de IF's.

'''
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('{}, as retas que você inseriu PODEM formar um triângulo!'.format(nome))
    triangulo = True
else:
    print('{}, as retas que você inseriu NÃO PODEM formar um triângulo!'.format(nome))
    triangulo = False

#print(triangulo)

if triangulo == False:
    print('Fim :D')  
elif reta1 == reta2 and reta2 == reta3:
    print('{}, as retas que você inseriu formam um Triângulo Equilátero!'.format(nome))
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('{}, as retas que você inseriu formam um Triângulo Isóceles!'.format(nome))
elif reta1 != reta2 and reta2 != reta3:
    print('{}, as retas que você inseriu formam um Triângulo Escaleno!'.format(nome))
'''
