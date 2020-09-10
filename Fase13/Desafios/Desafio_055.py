#   Fase 13 - Estrutura de repetição for
#   Desafio 55
#   Faça um programa que leia o peso de cinco pessoas.
#   No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 500
for c in range(0, 5):
    peso = float(input('Digite o peso da pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('')
print('{}Kg foi o peso maior lido.'.format(maior))
print('{}Kg foi o peso menor lido.'.format(menor))
