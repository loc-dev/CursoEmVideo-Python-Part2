#   Fase 12 - Condições Aninhadas
#   Desafio 40
#   Crie um programa que leia duas notas de um aluno
#   e calcule sua média, mostrando uma mensagem no final,
#   de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média entre 7.0 ou superior: APROVADO

nome = str(input('Digite o nome do Aluno(a): '))

nota01 = float(input('Digite a nota do 1º Bimestre de {}: '.format(nome)))
nota02 = float(input('Digite a nota do 2º Bimestre de {}: '.format(nome)))

media = (nota01 + nota02) / 2

if media < 5.0:
    print('{} ficou brincando na sala, então, infelizmente foi reprovado! Que feio!'.format(nome))
elif 5.0 < media < 6.9:
    print('{} não estudou muito, não fazia as atividades, então, está de recuperação!'.format(nome))
else:
    print('PARABÉNS, {}!!! Você esforçou muito e dedicou 100%, está APROVADO!'.format(nome))
