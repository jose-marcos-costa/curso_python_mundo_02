cores = {
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'limpa': '\033[m'
}

numero = int(input('Digite um número inteiro: '))
cont = 0
for i in range(1, numero+1):
    if numero % i == 0:
        cont += 1
if cont != 2:
    print('{}O número {} é NÃO É PRIMO!{}'.format( cores['vermelho'], numero, cores['limpa']))
else:
    print('{}O número {} é PRIMO!{}'.format(cores['verde'],numero, cores['limpa']))
