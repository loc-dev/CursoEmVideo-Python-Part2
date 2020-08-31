#   Fase 12 - Condições Aninhadas
#   Desafio 41
#   A Confederação Nacional de Natação precisa de um programa que leia
#   o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:

# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sénior
# - Acima : Master

from datetime import date

nome = str(input('Digite o nome do Atleta: '))
ano_nasc = int(input('Digite o ano de nascimento de {}: '.format(nome)))
idade = date.today().year - ano_nasc

# Categorias
if idade < 9:
    print('Sua categoria {} na Confederação Nacional de Natação: \nMIRIM'.format(nome))
elif 9 < idade < 14:
    print('Sua categoria {} na Confederação Nacional de Natação: \nINFANTIL'.format(nome))
elif 14 < idade < 19:
    print('Sua categoria {} na Confederação Nacional de Natação: \nJUNIOR'.format(nome))
elif 19 < idade == 20:
    print('Sua categoria {} na Confederação Nacional de Natação: \nSÊNIOR'.format(nome))
else:
    print('Sua categoria {} na Confederação Nacional de Natação: \nMASTER'.format(nome))
