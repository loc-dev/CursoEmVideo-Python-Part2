#   Fase 12 - Condições Aninhadas
#   Desafio 44
#   Elabore um programa que calcule o valor
#   a ser pago por um produto, considerando o seu preço normal
#   e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

nome_produto = str(input('Digite o nome do produto: '))
valor_produto = float(input('Digite o valor {}: R$ '.format(nome_produto)))
print('')
print('Opção de pagamento: \n'
      'Dinheiro/Cheque [ 1 ] \n'
      'Cartão          [ 2 ]')
alternativa = int(input('Qual é a sua opção de pagamento: '))

if alternativa == 1:
    desc = (valor_produto * 10) / 100
    print('')
    print('Sua opção de pagamento é Dinheiro/Cheque')
    print('Foi concedido um desconto de 10%')
    print('Valor Final: R$ {:.2f}'.format(valor_produto - desc))
elif alternativa == 2:
    print('')
    print('Sua opção de pagamento é Cartão')
    op = str(input('Deseja pagar à vista ou parcelado: '))
    op = op.replace(' ', '').upper().split()
    if 'VISTA' in op:
        desc = (valor_produto * 5) / 100
        print('Foi concedido um desconto de 5%')
        print('Valor Final: R$ {:.2f}'.format(valor_produto - desc))
    elif 'PARCELADO' in op:
        n_parc = int(input('Em quantas vezes: '))
        if n_parc <= 2:
            print('')
            print('Valor da compra em {}x de R$ {:.2f}'.format(n_parc, valor_produto))
        elif 3 <= n_parc < 24:
            print('')
            print('Valor da compra em {}x de R$ {:.2f}'.format(n_parc, valor_produto))
            print('Com juros de 20%')
            juros = ((20 / 100) * (valor_produto / n_parc))
            print('Valor de cada prestação: R$ {:.2f}'.format((valor_produto / n_parc) + juros))
            print('Valor Total: R$ {:.2f}'.format(valor_produto + (juros * n_parc)))
        else:
            print('Digitado incorretamente!')
            print('Tente novamente')
    else:
        print('Não existe essa categoria!')
        print('Tente novamente')
else:
    print('')
    print('Não foi encontrado está opção de pagamento!')
    print('Tente novamente')
