a1 = int(input('Primeiro termo da PA (a1): '))
r = int(input('Razão da PA (r): '))
cont = 1
termo = a1
while cont <=10:
    print('{}'.format(termo), end=' → ')
    termo += r
    cont += 1
print('ACABOU!')