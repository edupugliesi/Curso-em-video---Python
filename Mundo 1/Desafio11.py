#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
#pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

nome = str(input('\nQual o nome do pintor? '))
largura = float(input('Qual a largura da parede? '))
altura = float(input('E a altura? '))

areaTotal = largura*altura
tintaNecessaria = areaTotal/2

print('{}, a parede tem {} m² e será necessário {} litros de tinta para pintar.\n'.format(nome, areaTotal, tintaNecessaria))