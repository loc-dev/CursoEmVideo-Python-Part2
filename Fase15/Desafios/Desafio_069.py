#   Fase 15 - Interrompendo a estrutura de repetições while
#   Desafio 69
#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário
#   quer ou não continuar. No final, mostre:

#   A) Quantas pessoas tem mais de 18 anos.
#   B) Quantos homens foram cadastrados.
#   C) Quantas mulheres tem menos de 20 anos.

maiores_idade = qnt_homens = mulheres_jovens = 0

while True:
    print('-=-' * 15)
    idade = int(input('Digite a sua idade: '))  
    
    while True:
        sexo = str(input('Digite o sexo [M | F]: ')).strip().upper()

        if sexo in "MmFf":
            break

    if 18 < idade:
        maiores_idade += 1
        if sexo == "M":
            qnt_homens += 1
        elif 20 > idade:
            mulheres_jovens += 1
    elif 18 > idade:
        if sexo == "M":
            qnt_homens += 1
        elif sexo == "F":
            mulheres_jovens += 1
        
    print('-=-' * 15)
    print('PESSOA CADASTRADA COM SUCESSO!')
    print('-=-' * 15)

    while True:
        continuar = str(input('Deseja continuar [S | N]: ')).strip().upper()

        if continuar in "SsNn":
            break
    
    print()

    if continuar in "N":
        break

print(f'{"=" * 10} FIM DO PROGRAMA {"=" * 10}')
print(f'Temos cadastrado {maiores_idade} pessoas com mais de 18 anos.')
print(f'São {qnt_homens} homens cadastrados.')
print(f'E, {mulheres_jovens} mulher(es) com menos de 20 anos.')
