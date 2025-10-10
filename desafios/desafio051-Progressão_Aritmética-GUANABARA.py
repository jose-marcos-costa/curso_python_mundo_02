a1 = int(input('1º termo da PA: '))
r = int(input('Razão da PA: '))
n = 10
an = a1 + (n+1) * r
for i in range(a1, an + r, r):
    print('{}'.format(i), end=' → ')
print('ACABOU')
