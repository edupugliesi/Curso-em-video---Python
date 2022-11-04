def aumentar(p, t):
    final = p + (p * t/100)
    return f'O aumento de 10% sobre o valor digitado é {final}'

def diminuir(p, t):
    final = p - (p * t/100)
    return f'A redução de 10% sobre o valor digitado é {final}'

def dobro(p):
    final = p * 2
    return f'O dobro do valor digitado é {final}'

def metade(p):
    final = p / 2
    return f'A metade do valor digitado é {final}'
    