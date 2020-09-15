#   Fase 14 - Estrutura de repetição While - Parte 2
#   Desafio 57
#   Faça um programa que leia o sexo de uma pessoa, mas,
#   só aceite os valores 'M' ou 'F'. Caso esteja errado,
#   peça a digitação novamente até ter um valor correto.

sexo = 'none'

while 'M' != sexo != 'F':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
print('Você digitou: {}'.format(sexo))
