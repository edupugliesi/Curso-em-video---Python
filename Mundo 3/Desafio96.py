'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno
'''

def titulo(msg):
    print('='*len(msg))
    print(msg)
    print('='*len(msg))

def area():
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    area = 0
    area = largura * comprimento
    print(f'Comprimento do terreno é de {area} m²')
    
titulo('Calcular Área')
area()