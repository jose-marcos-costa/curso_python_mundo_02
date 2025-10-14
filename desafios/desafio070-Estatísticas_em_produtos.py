from functools import total_ordering

nome_mais_barato = ''
preco_mais_barato = 0.0
cont_mais_1000 = 0
controle = 'S'
total = 0.0
cont = 0
while controle == 'S':
    nome = str(input('Digite o nome do PRODUTO: ')).strip()
    preco = float(input('Digite o preço do PRODUTO: '))
    total += preco
    if cont == 0:
        preco_mais_barato = preco
        nome_mais_barato = nome
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            nome_mais_barato = nome
        if preco > 1000.0:
            cont_mais_1000 += 1
    controle = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Opção Inválida! Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
print(f'O total gasto foi de R$ {total}')
print(f'{cont_mais_1000} produtos custam mais de R$ 1000')
print(f'O produto mais barato é {nome_mais_barato}')
