numero = int(input('Digite um número: '))
print('{:=^20}'.format(' TABUADA '))
for i in range(1, 11):
    print('{} X {:2} = {}'.format(numero,i, numero*i ))
