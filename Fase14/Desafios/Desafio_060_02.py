#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 60
#   Faça um programa que leia um número qualquer
#   e mostre o seu fatorial.

# Ex : 5! = 5 x 4 x 3 x 2 x 1 = 120

#   Versão 02

n = int(input('Digite um número qualquer: '))
t = 0
ant = 0

if n >= 2:
    print()
    print('{}! ='.format(n), end=' ')
    for i in range(n, 0, -1):
        if i != 1:
            print('{} x'.format(i), end=' ')
            if i > ant:
                t = i
            else:
                t = t * i
        else:
            print('{} ='.format(i), end=' ')
            t = t * 1
        ant = i
    print(t)
else:
    print()
    print('{}! = 1'.format(n), end=' ')
