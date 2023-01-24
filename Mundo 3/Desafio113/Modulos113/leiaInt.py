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