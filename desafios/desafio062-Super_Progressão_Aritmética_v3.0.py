a1 = int(input('Primeiro termo da PA (a1): '))
r = int(input('Razão da PA: '))
aux = a1
n = 10
cont = 1
while n != 0:
    while cont <= n:
        an = a1 + (cont - 1) * r
        print('{}'.format(an), end=' → ')
        cont += 1
    print('ACABOU!')
    n = int(input('Quantos termos a mais você deseja visualizar? '))
    a1 = an + r
    cont = 1
print('FINISH')