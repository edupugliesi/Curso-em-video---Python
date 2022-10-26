'''
FAça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (Opcional)

Adiciona também docstrings da função'''

def texto(msg):
    linha = len(msg) + 4
    print()
    print('-' * linha)
    print(f'  {msg}')
    print('-' * linha)
    print()


def notas():
    turma = []
    alunos = {}
    
    count1 = 1
    
    texto('Alunos')
    
    while True:
        
        
        alunos['nome'] = str(input(f'{count1}º aluno: '))
        
        count2 = 1
        totalNotas = []
        
        texto('Notas')
        while True:
            
            nota = float(input(f'{count2}º nota: '))
            totalNotas.append(nota)
            
            print(totalNotas)
            
            op1 = str(input('Deseja adicionar mais notas? [S/N] ')).upper()
            if op1 == 'N':
                break
            
        
            count2 +=1
        
        alunos['nota'] = totalNotas.copy()
        
        texto('Alunos')
        
        turma.append(alunos.copy())
        alunos.clear()
        
        count1 += 1
        
        op2 = str(input('Deseja adicionar mais alunos? [S/N] ')).upper()
        if op2 == 'N':
            break
        
        
    texto('Resultado')
    print(turma)


notas()
        
        
        
        
        
        
