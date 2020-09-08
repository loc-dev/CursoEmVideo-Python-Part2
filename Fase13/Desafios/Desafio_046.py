#   Fase 13 - Estrutura de repetição for
#   Desafio 46
#   Faça um programa que mostre na tela uma contagem regressiva
#   para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
#   1 segundo entre eles.

import emoji
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:FELIZ ANO NOVO :two::one::zero::zero::fireworks: ', use_aliases=True))
