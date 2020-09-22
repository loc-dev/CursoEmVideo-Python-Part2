#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 65
#   Crie um programa que leia vários números inteiros pelo teclado.
#   No final da execução, mostre a média entre todos os valores
#   e qual foi o maior e o menor valores lidos. O programa deve perguntar
#   ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
soma_total = 0
qnts_vezes = 0
maior_n = 0
menor_n = 0

while resposta == 'S':
    numero = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()
    soma_total += numero
    qnts_vezes += 1
    if qnts_vezes == 1:
        maior_n = numero
        menor_n = numero
    else:
        if numero > maior_n:
            maior_n = numero
        elif numero < menor_n:
            menor_n = numero

print()
print('Foi digitado {} número(s)'.format(qnts_vezes))
print('Então a média entre todos os números será {:.2f}'.format(soma_total / qnts_vezes))
print('O maior valor digitado foi {}'.format(maior_n))
print('O menor valor digitado foi {}'.format(menor_n))
