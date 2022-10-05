'''
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente.
'''
aluno = []
turma = []

# Estrutura para preenchimento das listas com os alunos e as notas.
while True:
    aluno.append(str(input('Aluno: ')))
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    

    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
    # Função para sair do while
    if op != 'S':
        print('='*30)
        break
    
    print('-'*30)

count = 0

# Printar o boletim na tela.
for alunos in turma:
    print(f'Aluno {count}: {alunos[0]} // Média: {(alunos[1] + alunos[2])/2}')
    count += 1

print('='*30)

op2 = int(input('Digite o número do aluno para ver suas notas individuais: '))

# Validação para inserir um aluno válido
while op2 > len(turma) or op2 < 0:
    op2 = int(input('Aluno inexistente. Digite novamente: '))

# Printar a nota indivual do aluno selecionado.
print(turma[op2])