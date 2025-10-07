print('-#-' * 12)
print('Conversor de Bases Numéricas')
print('-#-' * 12)
num = int(input('Digite um número inteiro: '))
print('\nEscolha uma das opções abaixo:')
print('1 - Binário\n2 - Octal\n3 - Hexadecimal\n')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('O número inteiro {} corresponde ao número {} na base binária.'.format(num, bin(num)))
elif opcao == 2:
    print('O número inteiro {} corresponde ao número {} na base octal.'.format(num, oct(num)))
elif opcao == 3:
    print('O número inteiro {} corresponde ao número {} na base hexadecimal.'.format(num, hex(num)))
else:
    print('Opção Inválida!')

