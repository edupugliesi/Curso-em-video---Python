def aumentar(p = 0, t = 0):
    final = p + (p * t/100)
    return final

def diminuir(p = 0, t = 0):
    final = p - (p * t/100)
    return final

def dobro(p = 0):
    final = p * 2
    return final

def metade(p = 0):
    final = p / 2
    return final

def moeda(preço = 0, moeda = '', format=False):
    if format == True:
        moeda = 'R$'
        return f'{moeda}{preço:.2f}'.replace('.', ',')
    else:
        return f'{moeda}{preço}'
    
def resumo(valor, taxa):
    print('-')
    print(f'O valor aumentado em {taxa}% é {moeda(aumentar(valor, taxa), format=True)}')
    print(f'O valor diminuído em {taxa}% é {moeda(diminuir(valor, taxa), format=True)}')
    print(f'O dobro de {moeda(valor, format=True)} é {moeda(dobro(valor), format=True)}')
    print(f'A metade de {moeda(valor, format=True)} é {moeda(metade(valor), format=True)}')