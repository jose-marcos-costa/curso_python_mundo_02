numero = int(input('Digite um número: '))
cont = numero
fatorial = 1
print('{}! = '.format(numero), end='')
while cont >= 1:
    fatorial *= cont
    if cont != 1:
        print('{}'.format(cont), end='x')
    else:
        print('{}'.format(cont), end='')
    cont -= 1
print(' = {}'.format(fatorial))