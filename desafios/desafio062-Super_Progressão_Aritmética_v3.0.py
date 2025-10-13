a1 = int(input('Primeiro termo da PA (a1): '))
r = int(input('Razão da PA: '))
n = 10
cont = 1
total = 0
while n != 0:
    total = total + n
    while cont <= n:
        an = a1 + (cont - 1) * r
        print('{}'.format(an), end=' → ')
        cont += 1
    print('PAUSA!')
    n = int(input('Quantos termos a mais você deseja visualizar? '))
    a1 = an + r
    cont = 1
print('FINISH')
print('Progressão finalizada com {} termos mostrados.'.format(total))