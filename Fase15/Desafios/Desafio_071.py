#   Fase 15 - Interrompendo a estrutura de repetições while
#   Desafio 71
#   Crie um programa que simule o funcionamento de um caixa eletrônico.
#   No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#   e o programa vai informar quantas cédulas de cada valor serão entregues.

#   Obs.: Considere que o caixa possuí cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print('=' * 20)
print('{:^20}'.format('BANCO CEV'))
print('=' * 20)

print()
valor = int(input('Insira o valor que deseja: R$ '))
print('Esta máquina distribui notas de R$ 1, R$ 10, R$ 20 e R$ 50.')

resto = 0

valor = str(valor)


while True:

    if len(valor) >= 3: # Três casas ou mais
        valor = int(valor)
        if valor % 50 == 0: # Resto zero
            cedula = valor // 50
            print(f'Total de {cedula} cédulas de R$ 50')
        elif valor % 50 != 0: # Resto diferente de 0
            cedula = valor // 50
            resto = valor % 50
            valor = resto
            valor = str(valor)
            print(f'Total de {cedula} cédulas de R$ 50')

    
    elif len(valor) == 2: # Duas casas
        valor = int(valor)
        if valor >= 20:
            if valor % 20 == 0: # Resto zero
                cedula = valor // 20
                resto = valor % 20
                print(f'Total de {cedula} cédulas de R$ 20')
            elif valor % 20 != 0: # Resto diferente de 0
                cedula = valor // 20
                resto = valor % 20
                valor = resto
                valor = str(valor)
                print(f'Total de {cedula} cédulas de R$ 20')
        elif valor >= 10:
            if valor % 10 == 0: # Resto zero
                cedula = valor // 10
                resto = valor % 1
                print(f'Total de {cedula} cédulas de R$ 10')
            elif valor % 10 != 0: # Resto diferente de 0
                cedula = valor // 10
                resto = valor % 10
                valor = resto
                valor = str(valor)
                print(f'Total de {cedula} cédulas de R$ 10')

    elif len(valor) == 1: # Uma casa
        valor = int(valor)
        if valor < 10:
            if valor % 1 == 0: # Resto zero
                cedula = valor // 1
                resto = valor % 1
                print(f'Total de {cedula} cédulas de R$ 1')

    # Verificação de resto
    if resto != 0:
        True
    else:
        break   
    
print()
print('Volte sempre ao BANCO CEV!') 

