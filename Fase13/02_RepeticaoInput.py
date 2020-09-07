# Fase 13 - Estrutura de repetição For - Parte 1
# Prática

# Utilizando função input() para definir o valor da posição a parar
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

print('')

# Definindo a sintaxe da função range()
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
