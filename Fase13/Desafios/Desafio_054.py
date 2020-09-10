#   Fase 13 - Estrutura de repetição for
#   Desafio 54
#   Crie um programa que leia o ano de nascimento de sete pessoas.
#   No final, mostre quantas pessoas ainda não atingiram a maioridade
#   e quantas já são maiores.

from datetime import date

ano_nasc = 0
qnts_maiores = 0
qnts_menores = 0

for c in range(0, 7):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano_nasc

    if 21 <= idade:
        qnts_maiores += 1
    else:
        qnts_menores += 1

print('')
print('{} pessoa(s) ainda não atingiu/atingiram a maioridade.'.format(qnts_menores))
print('{} pessoa(s) já é/são maior(es) de idade.'.format(qnts_maiores))
