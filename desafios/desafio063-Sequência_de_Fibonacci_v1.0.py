n_termos = int(input('Digite o número de termos da Sequência de Fibonacci: '))
cont = 0
fibonacci= [0, 1]
aux1 = 0
aux2 = 0
while cont < n_termos:
    if  cont == 0:
        print('{}'.format(fibonacci[cont]), end=' → ')
    elif cont == 1:
        print('{}'.format(fibonacci[cont]), end=' → ')
    elif cont >=  2:
        fibonacci.append(fibonacci[cont-2] + fibonacci[cont-1])
        print('{}'.format(fibonacci[cont]), end=' → ')
    cont += 1
print('ACABOU!')
#print(fibonacci)