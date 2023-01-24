'''Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma pessoa e listar todas as pessoas cadastradas'''

from Modulos115.interface import *
from Modulos115.arquivo import *
from time import sleep

arq = 'banco.txt'

if not arqExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    
    if resposta == 1:
        #Opção para listar o conteúdo do arquivo banco.txt
        lerArquivo(arq)
        print('\n')

    elif resposta == 2:
        header('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        print('\n')
        
    elif resposta == 3:
        header('Saindo do sistema.')
        print('\n')
        break

    else:
        print('\033[31mDigite uma opção válida.\033[m')

    sleep(1)