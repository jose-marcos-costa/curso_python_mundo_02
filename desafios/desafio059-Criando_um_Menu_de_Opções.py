numero1 = int(input('Digite o primero valor: '))
numero2 = int(input('Digite o segundo valor: '))
print('{:=^30}'.format(' OPÇÕES '))
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
opcao = int(input('Opção escolhida: '))
print('{:=^30}'.format('='))
while opcao != 5:
    if opcao == 1:
        print('O resultado da soma é {}'.format(numero1 + numero2))
    elif opcao == 2:
        print('O resultado da multiplicação é {}'.format(numero1 * numero2))
    elif opcao == 3:
        if numero1 > numero2:
            print('{} é maior que {}'.format(numero1, numero2))
        elif numero2 > numero1:
            print('{} é maior que {}'.format(numero2, numero1))
        else:
            print('Os números são IGUAIS!')
    elif opcao == 4:
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
    print('{:=^30}'.format(' OPÇÕES '))
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opcao = int(input('Opção escolhida: '))
    print('{:=^30}'.format('='))
