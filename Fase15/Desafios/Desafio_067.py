#   Fase 15 - Interrompendo a estrutura de repetições While
#   Desafio 67
#   Faça um programa que mostre a tabuada de vários números, um de cada vez,
#   para cada valor digitado pelo usuário. O programa será interrompido quando
#   o número solicitado for negativo.

while True:
    print('-=' * 8)
    n = int(input('Digite o valor da seguinte Tabuada: '))
    print('-=' * 8)
    
    if 0 > n:
        break
    for i in range(1, 11):
        print(f'{n} x {i:<2} = {n*i}')

print('TABUADA INDISPONÍVEL!')
