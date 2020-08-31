#   Fase 12 - Condições Aninhadas
#   Desafio 43
#   Desenvolva uma lógica que leia o peso
#   e a altura de uma pessoa, calcule seu IMC
#   e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

nome = str(input('Digite o seu nome: '))
peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura ** 2)

print('')

if imc < 18.5:
    print('RESULTADO: {:.1f}'.format(imc))
    print('{} você está: ABAIXO DO PESO'.format(nome))
elif 18.5 < imc < 25:
    print('RESULTADO: {:.1f}'.format(imc))
    print('{} você está: PESO IDEAL'.format(nome))
elif 25 < imc < 30:
    print('RESULTADO: {:.1f}'.format(imc))
    print('{} você está: SOBREPESO'.format(nome))
elif 30 < imc < 40:
    print('RESULTADO: {:.1f}'.format(imc))
    print('{} você está: OBESIDADE'.format(nome))
else:
    print('RESULTADO: {:.1f}'.format(imc))
    print('{} você está: OBESIDADE MÓRBIDA'.format(nome))
