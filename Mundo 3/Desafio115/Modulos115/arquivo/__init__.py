from Modulos115.interface import header


#Verificar se o arquivo banco.txt existe
def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else: 
        return True


#Criar o arquivo banco.txt
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


#Ler conteúdo do arquivo banco.txt
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        header('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


#Cadastrar conteúdo no arquivo banco.txt
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados.')
        else:
            print(f'\nNovo registro adicionado!')
            a.close()

