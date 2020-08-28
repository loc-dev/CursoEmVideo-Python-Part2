#   Fase 12 - Condições Aninhadas
#   Desafio 37
#   Escreva um programa que leia um número inteiro qualquer
#   e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))

print('')
print('Escolha uma conversão: \nBinário [1] \nOctal [2] \nHexadecimal [3]')
op = int(input('Digite a opção desejada: '))
print('')

if op == 1:
    print('Binário: ', bin(num).replace('0b', ''))
    print('')
elif op == 2:
    print('Octal: ', oct(num).replace('0o', ''))
    print('')
elif op == 3:
    print('Hexadecimal: ', hex(num).replace('0x', ''))
    print('')
else:
    print('Saindo do programa...')
