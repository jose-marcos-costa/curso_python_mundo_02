numero = int(input('Digite um número: '))
print('{:=^20}'.format(' TABUADA '))
for i in range(1, 11):
    print('{:2} X {:2} = {}'.format(i, numero, i * numero))
