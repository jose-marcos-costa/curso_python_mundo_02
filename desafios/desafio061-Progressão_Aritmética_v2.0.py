a1 = int(input('Primeiro termo da PA (a1): '))
r = int(input('Razão da PA (r): '))
cont = 1
while cont <=10:
    an = a1 + (cont - 1) * r
    print('{}'.format(an), end=' → ')
    cont += 1
print('ACABOU!')