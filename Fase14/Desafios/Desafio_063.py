#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 63
#   Escreva um programa que leia um número n inteiro qualquer
#   e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

# Ex : 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Digite um número inteiro: '))
p = 0
Fa = 0
Fp = 0

while p <= n:
    if Fp == 0:
        print(Fp, end=' ')
        Fa = Fp
        Fp = 1
    else:
        if 1 <= p <= 2:
            Fa = Fp
            print(Fp, end=' ')
        else:
            Fs = Fa + Fp
            print(Fs, end=' ')
            Fa = Fp
            Fp = Fs
    p = p + 1
