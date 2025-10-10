soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(i)))
    if numero % 2  == 0:
        soma += numero
        cont += 1
if cont == 0:
    print('Nenhum número par foi digitado!')
else:
    print('Você informou {} números PARES e a soma deles foi {}'.format(cont, soma))