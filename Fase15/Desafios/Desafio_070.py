#   Fase 15 - Interrompendo a estrutura de repetições while
#   Desafio 70
#   Crie um programa que leia o nome e o preço de vários produtos.
#   O programa deverá perguntar se o usuário vai continuar.
#   No final, mostre:

#   A) Qual é o total gasto na compra.
#   B) Quantos produtos custam mais de R$1000.00.
#   C) Qual é o nome do produto mais barato.

total_compra = 0.00
cont = 0
produto_caro = 0
saved_nome = 'none'

print('-' * 15)
print('   LOJA 10   ')
print('-' * 15)

while True:
    print()
    nome_produto = str(input('Digite o nome do produto: ')).strip()
    preco_produto = float(input('Digite o preço do produto: R$ '))

    # O total gasto na compra
    total_compra += preco_produto
    
    # Quantos produtos custam mais de R$ 1000.00
    if preco_produto > 1000.00:
        produto_caro += 1
    
    # Qual é o nome do produto mais barato
    cont += 1
    
    if cont == 1:
        preco_maior = preco_produto
        preco_menor = preco_produto
        saved_nome = nome_produto
    else:
        if preco_produto > preco_maior:
            preco_maior = preco_produto
        elif preco_produto < preco_menor:
            preco_menor = preco_produto
            saved_nome = nome_produto

    # Perguntar ao usuário se deseja continuar registrando a compra
    continuar = str(input('Deseja continuar? [S | N] ')).strip().upper()
    
    if continuar in "Ss":
        True
    else:
        break

print()
print('----- Relatório da compra -----')
print(f'Total da compra: R$ {total_compra:.2f}')
print(f'Temos {produto_caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {saved_nome} que custa {preco_menor:.2f}')
