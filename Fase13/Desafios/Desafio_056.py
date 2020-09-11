#   Fase 13 - Estrutura de repetição for
#   Desafio 56
#   Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#   No final do programa, mostre:

# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

s_idade = 00.00
m_idade = 00.00

saved_man_nome = 'none'
# saved_woman_nome = 'none'

old_man_age = 0

sum_woman_age = 0

for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (masculino | feminino): '))
    print('')

    s_idade += idade
    m_idade = s_idade / 4

    sexo = sexo.replace(' ', '').upper().split()

    if sexo == ['MASCULINO']:
        if idade > old_man_age:
            old_man_age = idade
            saved_man_nome = nome

    elif sexo == ['FEMININO']:
        if idade < 20:
            sum_woman_age += 1

print('A média de idade do grupo é: {:.2f}'.format(m_idade))
print('Homem mais velho: {}'.format(saved_man_nome))
print('Tem {} mulher(es) com menos de 20 anos'.format(sum_woman_age))
