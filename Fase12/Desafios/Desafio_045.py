#   Fase 12 - Condições Aninhadas
#   Desafio 45
#   Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('-=' * 8)
print('Jokenpó')
print('=-' * 8)
print('''Como jogar:
Pedra   [1]
Papel   [2]
Tesoura [3]''')
print('')
print('\033[4;32mRegras\033[m: \n'
      '\033[1;30mPedra\033[m ganha de \033[1;30mTesoura\033[m \n'
      '\033[1;30mTesoura\033[m ganha do \033[1;30mPapel\033[m \n'
      '\033[1;30mPapel\033[m ganha da \033[1;30mPedra\033[m')

print('')
print('Caso os dois jogadores façam a mesma opção, ocorre um \033[1;33mEmpate\033[m.')

print('')
print('Preparados para jogar?')
sleep(5)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('')

computador = randint(1, 3)
computador = str(computador)

jogador = int(input('Qual é a sua opção: '))
jogador = str(jogador)


if computador == "1" and jogador == "2":
    print('Computador <- Pedra vs Papel -> Jogador')
    print('Parabéns, você ganhou!!!')
elif computador == "1" and jogador == "3":
    print('Computador <- Pedra vs Tesoura -> Jogador')
    print('Puts, você perdeu!')
elif computador == "2" and jogador == "1":
    print('Computador <- Papel vs Pedra -> Jogador')
    print('Puts, você perdeu!')
elif computador == "2" and jogador == "3":
    print('Computador <- Papel vs Tesoura -> Jogador')
    print('Parabéns, você ganhou!!!')
elif computador == "3" and jogador == "1":
    print('Computador <- Tesoura vs Pedra -> Jogador')
    print('Parabéns, você ganhou!!!')
elif computador == "3" and jogador == "2":
    print('Computador <- Tesoura vs Papel -> Jogador')
    print('Puts, você perdeu!')
elif computador == jogador:
    if '1' in computador and jogador:
        print('Computador <- Pedra vs Pedra -> Jogador')
    elif '2' in computador and jogador:
        print('Computador <- Papel vs Papel -> Jogador')
    else:
        print('Computador <- Tesoura vs Tesoura -> Jogador')
    print('Empate!')
else:
    print('Opção incorreta')
    print('Tente de novo!')
