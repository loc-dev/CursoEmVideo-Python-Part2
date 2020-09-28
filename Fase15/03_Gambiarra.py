# Fase 15 - Interrompendo a estrutura de repetições While
# Prática

# A gambiarra

n = s = 0

while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
