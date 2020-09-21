#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 64
#   Crie um programa que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999,
#   que é a condição de parada. No final, mostre quantos números
#   foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Para finalizar o programa \ndigite o valor 999.')
print()

n = 0
x = 0
s = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        x += 1
        s += n

print('Número de vezes digitado um valor {}.\nA soma entre os números digitado foi {}!'.format(x, s))
