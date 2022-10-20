'''
Faça um programaq ue tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptavel.

Ex: ecreva('Olá Mundo')

saída

---------
Olá mundo
---------
'''

def mensagem(msg):
    print('#'*len(msg))
    print(msg)
    print('#'*len(msg))

mensagem(str(input('Digite a mensagem que deseja mostrar: ')))