'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo!
'''

print('-'*30)
print('Vamos fazer uma tabuada!')
print('-'*30)

n = 0
resultado = 0
tabuada = 0
count = 0

#Looping infinito com parâmentro N < 0 parar interromper. Estrutura responsável para capturar o N.
while True:
    n = int(input('Digite um número (Número negativo para parar): '))
    
    if n < 0:
        break
    
    #Looping infinito com parâmetro tabuada == 11 para interromper. Estrutura responsável para fazer a tabuada
    while True:
        resultado = n * tabuada
        print(f'{n} x {tabuada} = {resultado}')
        tabuada += 1
        
        #IF para interrupção do Looping e zerar o contador tabuada
        if tabuada == 11:
            tabuada = 0
            break
        
    count += 1
    
print(f'Fim, você fez a tabuada de {count} números!')