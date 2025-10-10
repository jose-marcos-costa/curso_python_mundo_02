cores = {
    'vermelho': '\033[1;30;41m',
    'verde': '\033[1;30;42m',
    'amarelo': '\033[1;34m',
    'azul': '\033[0;33m',
    'limpa': '\033[m'
}

numero = int(input('Digite um número inteiro: '))
cont = 0
for i in range(1, numero+1):
    if numero % i == 0:
        cont += 1
        print(cores['amarelo'], end='')
    else:
        print(cores['azul'], end='')
    print('{} '.format(i), end='')
if cont != 2:
    print('\n{}O número {} é NÃO É PRIMO!{}'.format( cores['vermelho'], numero, cores['limpa']))
else:
    print('\n{}O número {} é PRIMO!{}'.format(cores['verde'],numero, cores['limpa']))
