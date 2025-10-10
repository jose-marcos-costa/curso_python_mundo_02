a1 = int(input('1º termo da PA: '))
r = int(input('Razão da PA: '))
n = 10
for i in range(1, n+1):
    an = a1 + (i-1) * r
    #print('O {}º termo da PA é {}'.format(i, an))
    print('{}'.format(an), end=' → ')
print('ACABOU')
