#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 58
#   Melhore o jogo do Desafio 028 onde o computador vai
#   "pensar" em um número entre 0 e 10. Só que agora o jogador vai
#   tentar adivinhar até acertar, mostrando no final quantos palpites
#   foram necessários para vencer.

from random import randint

computador = randint(0, 10)
qnts_palpites = 0

print('-=-' * 8)
print('O que estou pensando...')
print('-=-' * 8)

usuario = 11

print()

while computador != usuario:
    usuario = int(input('Digite o número que o computador está pensando: '))
    qnts_palpites += 1

print('')
print('PARABÉNS! Você venceu!')

if qnts_palpites > 1:
    print('Foram necessários {} palpites para vencer do computador!'.format(qnts_palpites))
else:
    print('Foi necessário {} palpite para vencer do computador!'.format(qnts_palpites))
