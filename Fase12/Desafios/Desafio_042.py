#   Fase 12 - Condições Aninhadas
#   Desafio 42
#   Refaça o Desafio 35 dos triângulos, acrescentando o recurso
#   de mostrar que tipo de triângulo será formado:

# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

retaAB = float(input('Qual é o comprimento da reta AB (cm): '))
retaCD = float(input('Qual é o comprimento da reta CD (cm): '))
retaEF = float(input('Qual é o comprimento da reta EF (cm): '))

if retaAB + retaCD > retaEF and retaAB + retaEF > retaCD and retaEF + retaCD > retaAB:
    print('Pode ser um triângulo!')
    if retaAB == retaCD == retaEF:
        print('O triângulo é Equilátero!')
    elif retaAB == retaCD or retaAB == retaEF or retaEF == retaCD:
        print('O triângulo é Isósceles!')
    else:
        print('É um triângulo Escaleno!')
else:
    print('Não pode ser formado um triângulo!')


