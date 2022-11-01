def aumentar(n):
    final = n + (n * 0.10)
    return f'O aumento de 10% sobre o valor digitado é {final}'

def diminuir(n):
    final = n - (n * 0.10)
    return f'A redução de 10% sobre o valor digitado é {final}'

def dobro(n):
    final = n * 2
    return f'O dobro do valor digitado é {final}'

def metade(n):
    final = n / 2
    return f'A metade do valor digitado é {final}'

def moeda(n = float):
    return f'R${n:.2f}'
    