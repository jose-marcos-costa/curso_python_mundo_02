cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para sair]: '))
    if numero == 999:
        print(f'SAINDO...')
        break
    soma += numero
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')