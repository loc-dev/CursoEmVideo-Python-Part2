#   Fase 15 - Interrompendo a estrutura de repetições While
#   Desafio 66
#   Crie um programa que leia vários números inteiros pelo teclado.
#   O programa só vai parar quando o usuário digitar o valor 999,
#   que é a condição de parada. No final, mostre quantos números foram digitados
#   e qual foi a soma entre eles (desconsiderando o flag)

n = s = c = 0

while n != 999:
    n = int(input('Digite um número [999 -> Para sair do programa] : '))
    if n == 999:
        break
    s += n
    c += 1

print(f'A soma dos {c} valores digitados é {s}.')
