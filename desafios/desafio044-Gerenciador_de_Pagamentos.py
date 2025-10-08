print('{:=^40}'.format(' LOJAS DO ZÉ '))
valor_compra = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] - À Vista (Dinheiro/Cheque)
[ 2 ] - À Vista (Cartão)
[ 3 ] - Em até 2 vezes (Cartão)
[ 4 ] - Em 3 vezes ou mais (Cartão)''')
opcao_escolhida = int(input('Qual é a opção: '))
if 1 <= opcao_escolhida <=4:
    if opcao_escolhida == 1:
        total = valor_compra * (1 - 10 / 100)
    elif opcao_escolhida == 2:
        total = valor_compra * (1 - 5 / 100)
    elif opcao_escolhida == 3:
        parcelas = int(input('Quantas parcelas? '))
        total = valor_compra
        valor_parcelas = total / parcelas
        print('Sua compra será parcelada em {}x de {:.2f} SEM JUROS.'.format(parcelas, valor_parcelas))
    elif opcao_escolhida == 4:
        parcelas = int(input('Quantas parcelas? '))
        total = valor_compra * (1 + 20 / 100)
        valor_parcelas = total / parcelas
        print('Sua compra será parcelada em {}x de {:.2f} COM JUROS.'.format(parcelas, valor_parcelas))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor_compra, total))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO! Tente novamente...')

