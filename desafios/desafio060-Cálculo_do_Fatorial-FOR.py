numero = int(input('Digite um número: '))
fatorial = 1
print('{}! = '.format(numero), end='')
for i in range(numero, 0, -1):
    fatorial *= i
    if i != 1:
        print('{}'.format(i), end='x')
    else:
        print('{}'.format(i), end='')
print(' = {}'.format(fatorial))