#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 61
#   Refaça o Desafio 051, lendo o primeiro termo e razão de uma PA,
#   mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a sua razão: '))

print()
print('Os 10 primeiros termos dessa progressão: ')

print()
n = -1
an = 0

while n < 9:
    n = n + 1
    an = a1 + (n * r)
    print(an)
