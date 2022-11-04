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

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
    