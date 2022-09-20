frase = '   olá mundo   '
print(frase[::2]) # Mostra os caracteres nos indices pares
print(len(frase)) # Saber o comprimento dessa string
print(frase.count('o')) # Contar a quantidade de elementos na string
print(frase.find('mun')) # Achar elementos na string
print('mundo' in frase) # Achar elementos na string forma 2
print(frase.replace('olá', 'ALÔ')) # Subistituir elementos na string
print(frase.upper()) # Passar toda a string para maiúsculo
print(frase.capitalize()) # Coloca apenas a primeira letra da string em maiúsculo
print(frase.title()) # Coloca todas as primeiras letras em maiúsculo, caso a string tiver várias palavras.
print(frase.strip()) # Retira todos os espaços do início e do final da string.
print(frase.split()) # Reparte a string por palavras
print('-'.join(frase)) # Adiciona um elemento entre as palavras de um objeto para formar uma string