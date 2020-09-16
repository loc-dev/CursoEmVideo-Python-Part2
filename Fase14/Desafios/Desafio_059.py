#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 59
#   Crie um programa que leia dois valores
#   e mostre um menu na tela:

#   [ 1 ] Somar
#   [ 2 ] Multiplicar
#   [ 3 ] Maior
#   [ 4 ] Novos números
#   [ 5 ] Sair do programa

#   Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

op = 0

while op != 5:
    print()
    print('=' * 50)
    print('''Escolha as seguintes opções:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior número
[ 4 ] Digitar novos números
[ 5 ] Sair do programa''')
    print()
    op = int(input('{:^28}'.format('Que opção você deseja:')))

    if op == 1:
        print('_' * 35)
        print('Você escolheu a opção 1')
        print('.' * 22)
        print('{:^10.2f} + {:^10.2f}'.format(n1, n2))
        print('O resultado é: {:.2f}'.format(n1 + n2))
        print('.' * 22)
    elif op == 2:
        print('_' * 35)
        print('Você escolheu a opção 2')
        print('.' * 22)
        print('{:^10.2f} * {:^10.2f}'.format(n1, n2))
        print('O resultado é: {:.2f}'.format(n1 * n2))
        print('.' * 22)
    elif op == 3:
        print('_' * 35)
        print('Você escolheu a opção 3')
        print('.' * 22)
        if n1 == n2:
            print('Os dois valores são iguais!')
        elif n1 > n2:
            print('O valor maior é: {:.2f}'.format(n1))
        else:
            print('O valor maior é: {:.2f}'.format(n2))
        print('.' * 22)
    elif op == 4:
        print('_' * 35)
        print('Você escolheu a opção 4')
        print('.' * 22)
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print('.' * 22)
    elif op == 5:
        print('_' * 35)
        print('Você escolheu a opção 5')
        print('.' * 22)
        for c in range(0, 1):
            print('Finalizando', end='')
            for i in range(1, 4):
                print(end='.')
                sleep(0.6)
        print()
    else:
        print()
        print('Tente novamente, opção incorreta!')
        sleep(0.8)
