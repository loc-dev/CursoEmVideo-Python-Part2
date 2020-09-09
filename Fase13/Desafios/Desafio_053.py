#   Fase 13 - Estrutura de repetição for
#   Desafio 53
#   Crie um programa que leia uma frase qualquer
#   e diga se ela é um palíndromo, desconsiderando os espaços.

# Ex :
# APOS A SOPA -> APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

string = str(input('Digite uma frase qualquer (Sem acentos e vírgulas): '))

string = string.replace(' ', '').upper()
palin = string[::-1]

if string == palin:
    print('')
    print('{} -> {} são Palíndromos'.format(string, palin))
else:
    print('')
    print('Não forma um Palíndromo')
