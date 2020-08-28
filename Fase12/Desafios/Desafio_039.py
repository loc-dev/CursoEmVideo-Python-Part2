#   Fase 12 - Condições Aninhadas
#   Desafio 39
#   Faça um programa que leia o ano de nascimento de um jovem
#   e informe, de acordo com a sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

#   Seu programa também deverá mostrar o tempo que falta
#   ou que passou do prazo.

from datetime import date

nome = str(input('Digite o nome do jovem: '))
ano_nasc = int(input('Digite o ano de nascimento de {}: '.format(nome)))

idade = date.today().year - ano_nasc

if idade < 18:
    print('O {} ainda vai se alistar ao serviço militar.'.format(nome))
    print('Falta: {} anos'.format(18 - idade))
elif idade == 18:
    print('É a vez do {} se alistar ao serviço militar!'.format(nome))
    print('Se alista agora!')
else:
    print('Já passou o tempo do alistamento, {}.'.format(nome))
    print('Olha, já passou {} anos do seu alistamento!'.format(idade - 18))
