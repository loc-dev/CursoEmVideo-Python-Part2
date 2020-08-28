#   Fase 12 - Condições Aninhadas
#   Desafio 36
#   Escreva um programa para aprovar o empréstimo bancário
#   para a compra de uma casa. O programa vai perguntar o
#   o valor da casa, o salário do comprador e em quantos anos
#   ele vai pagar.

#   Calcule o valor da prestação mensal, sabendo que ela não pode
#   exceder 30% do salário ou então o empréstimo será negado.

nome = str(input('Digite o nome do comprador: '))
salario = float(input('Digite o salário de {}: R$ '.format(nome)))
imovel = float(input('Digite o valor do imóvel: R$ '))
prazo = int(input('Qual será o prazo: '))

valor_anual = imovel / prazo
valor_mensal = valor_anual / 12

if (valor_mensal * 100) / salario <= 30.00:
    print('')
    print('Empréstimo Solicitado, você pode financiar este imóvel!')
else:
    print('')
    print('Infelizmente, o empréstimo foi negado!')
