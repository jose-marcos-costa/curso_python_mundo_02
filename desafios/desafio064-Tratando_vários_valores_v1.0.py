numero = 0
cont = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    else:
        soma += numero
        cont += 1
print('\n{} números foram digitados e a soma entre eles é {}'.format(cont, soma))