# Fase 14 - Estrutura de repetição While - Parte 2
# Prática

# Um outro exemplo, usando condição de parada

r = 'S'

while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ? ')).upper()
print('Fim')
