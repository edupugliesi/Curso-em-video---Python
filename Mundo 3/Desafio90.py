'''
Faça um programa que leia nome e média de um aluno guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela
'''

print('='*30)

aluno = {}
turma = []

while True:
    
    aluno['nome'] = str(input('Aluno: '))
    aluno['media'] = float(input('Média: '))
    
    if aluno['media'] < 6:
        aluno['situação'] = 'Reprovado'
    elif aluno['media'] >= 6:
        aluno['situação'] = 'Aprovado'
    
    turma.append(aluno.copy())
    
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    
    
    
    if op == 'N':
        print('='*30)
        break
    
    print('-'*30)
    
print(turma)

for a in turma:
    for n, m, s in a.items():
        print(f'O aluno {n} tem uma média {m} e sua situação é {s}')
print('Fim')