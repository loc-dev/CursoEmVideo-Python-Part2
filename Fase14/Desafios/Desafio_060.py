#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 60
#   Faça um programa que leia um número qualquer
#   e mostre o seu fatorial.

# Ex : 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número qualquer: '))
t = 0
ant = 0

if n >= 2:
    print()
    print('{}! ='.format(n), end=' ')
    while n != 0:
        if n != 1:
            print('{} x'.format(n), end=' ')
            if n > ant:
                t = n
            else:
                t = t * n
        else:
            print('{} ='.format(n), end=' ')
            t = t * 1
        ant = n
        n = n - 1
    print(t)

else:
    print()
    print('{}! = 1'.format(n), end=' ')
