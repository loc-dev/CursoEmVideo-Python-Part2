#   Fase 13 - Estrutura de repetição for
#   Desafio 51
#   Desenvolva um programa que leia o primeiro termo
#   e a razão de uma progressão aritmética (PA).
#   No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a sua razão: '))

print('')
print('Os 10 primeiros termos dessa progressão:')
print(a1)
for c in range(0, 9):
    a1 = a1 + r
    print(a1)
