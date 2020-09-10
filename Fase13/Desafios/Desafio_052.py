#   Fase 13 - Estrutura de repetição for
#   Desafio 52
#   Faça um programa que leia um número inteiro
#   e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
qnts_vezes = 0

for c in range(1, n+1):
    if n % c == 0:
        qnts_vezes += 1

if qnts_vezes == 2:
    print('{} É número primo.'.format(n))
else:
    print('{} NÃO É número primo.'.format(n))
