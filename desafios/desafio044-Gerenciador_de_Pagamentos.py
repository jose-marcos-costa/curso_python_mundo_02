preco_normal = float(input('Digite o preço normal do produto: R$ '))
print('Escolha uma das opções de pagamento abaixo:')
print('0 - À Vista (Dinheiro/Cheque)')
print('1 - À Vista (Cartão)')
print('2 - Em até 2 vezes (Cartão)')
print('3 - Em 3 vezes ou mais (Cartão)')
opcao_escolhida = int(input('Digite a opção desejada: '))
if opcao_escolhida == 0:
    valor_a_pagar = preco_normal * (1 - 10/100)
    print('O valor a pagar é {:.2f}'.format(valor_a_pagar))
elif opcao_escolhida == 1:
    valor_a_pagar = preco_normal * (1 - 5/100)
    print('O valor a pagar é {:.2f}'.format(valor_a_pagar))
elif opcao_escolhida == 2:
    valor_a_pagar = preco_normal
    print('O valor a pagar é {:.2f}'.format(valor_a_pagar))
elif opcao_escolhida == 3:
    valor_a_pagar = preco_normal* (1 + 20/100)
    print('O valor a pagar é {:.2f}'.format(valor_a_pagar))
else:
    print('Opção Inválida!')
