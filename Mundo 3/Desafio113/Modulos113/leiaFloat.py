def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\nPor favor, digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('\nO usuário não informou um número.')
            return 0
        else:
            return n