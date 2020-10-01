# Fase 15 - Interrompendo a estrutura de repetições While
# Prática

# Aplicando o sentido do comando break

n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

# Método da string .format()
# print('A soma vale {}'.format(s))

# f-strings
print(f'A soma vale {s}')
