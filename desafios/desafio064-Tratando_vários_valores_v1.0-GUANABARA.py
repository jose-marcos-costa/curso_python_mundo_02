numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('\n{} números foram digitados e a soma entre eles é {}'.format(cont, soma))