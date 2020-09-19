#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 62
#   Melhore o Desafio 061, perguntando para o usuário
#   se ele quer mostrar mais alguns termos. O programa encerra
#   quando ele disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a sua razão: '))

print()
print('Os 10 primeiros termos dessa progressão: ')

print()
n = -1
an = 0
x = 1

while n < 9:
    n = n + 1
    an = a1 + (n * r)
    print(an)

if n == 9:
    while x != 0:
        print()
        x = int(input('Você deseja mais quantos termos desta progressão: '))
        print()
        if x != 0:
            prox_n = n + x
            while n < prox_n:
                n = n + 1
                an = an + r
                print(an)
            n = prox_n
        else:
            print('Você digitou {} termos'.format(x))
            print('Portanto, estou finalizando o programa!')
