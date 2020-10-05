#   Fase 15 - Interrompendo a estrutura de repetições while
#   Desafio 68
#   Faça um programa que jogue par ou ímpar com o computador.
#   O jogo só será interrompido quando o jogador perder, mostrando
#   o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

op_jogador = op_computador = resultado = ""
computador = jogador = soma = vitoria = 0

print('-=-'* 5)
print("PAR OU ÍMPAR")

while True:
    print('-=-'*5)
    op_jogador = str(input('Digite Par ou Ímpar [P | I]: '))
    jogador = int(input('Digite um número de 0 à 10: '))
    computador = randint(0, 10)
    print('-=-'*5)

    if op_jogador in "PpPar":
        op_jogador = "PAR"
        op_computador = "IMPAR"
    else:
        op_jogador = "IMPAR"
        op_computador = "PAR"

    soma = computador + jogador
    print(f'O jogador escolheu o número {jogador}, e, o computador número {computador}.')
    print(f'A soma dos números é {soma}.')

    if soma % 2 == 0:
        resultado = "PAR"
        if op_jogador == resultado and resultado != op_computador:
            print("Você ganhou, meus parabéns!")
            vitoria += 1
        else:
            print("Você perdeu, tenta novamente!")
            break
    else:
        resultado = "IMPAR"
        if op_jogador == resultado and resultado != op_computador:
            print("Você ganhou, meus parabêns!")
            vitoria += 1
        else:
            print("Você perdeu, tenta novamente!")
            break

if vitoria > 0:
    print(f'Você fez {vitoria} vitória(s) consecutiva(s).')
else:
    print(f'Não foi dessa vez, mas, não desista!')
