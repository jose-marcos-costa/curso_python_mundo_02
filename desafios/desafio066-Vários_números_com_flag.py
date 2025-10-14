cont = soma = numero = 0
while numero != 999:
    numero = int(input('Digite um número [999 para sair]: '))
    if numero == 999:
        print(f'SAINDO...')
        break
    else:
        soma += numero
        cont += 1
print(f'Foram digitados {cont} e a soma entre eles é {soma}')