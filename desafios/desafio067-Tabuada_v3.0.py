while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print(f'Finalizando...')
        break
    print('-=' * 10)
    for i in range (1, 11):
        print(f'{numero} x {i:2} = {numero * i}')
    print('-=' * 10)
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
