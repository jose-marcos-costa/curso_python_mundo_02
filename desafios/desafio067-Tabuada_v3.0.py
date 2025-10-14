numero = 0
while not numero < 0:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print(f'Finalizando...')
        break
    else:
        for i in range (1, 11):
            resultado = numero * i
            print(f'{numero} x {i:2} = {resultado}')
    print('-=' * 10)

