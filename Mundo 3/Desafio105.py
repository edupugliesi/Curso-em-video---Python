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

def notas(*n, sit=False):
    """
    > Função para analisar notas e situações de vários alunos
    N = Uma ou mais notas dos alunos (Aceita várias)
    SIT = Valor opcional para indicar a situação da turma
    RETURN = Retorna dicionário com as informações sobre a turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        elif r['média'] < 5:
            r['situação'] = 'RUIM'
    
    return r

resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
#help(notas)