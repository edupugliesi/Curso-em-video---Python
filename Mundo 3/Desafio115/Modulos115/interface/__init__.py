def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\nPor favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nO usuário não informou um número')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def header(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    header('Menu Principal')
    c = 1

    for item in lista:
        print(f'{c} - {item}')
        c +=1
        
    print(linha())

    op = leiaInt('Sua Opção: ')
    return op