print('-#-' * 12)
print('Conversor de Bases Numéricas')
print('-#-' * 12)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:')
[ 1 ] - converter para Binário
[ 2 ] - converter para Octal
[ 3 ] - converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número inteiro {} corresponde ao número {} na base binária.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número inteiro {} corresponde ao número {} na base octal.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número inteiro {} corresponde ao número {} na base hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida! Tente novamente...')

