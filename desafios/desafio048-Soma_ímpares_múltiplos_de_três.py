soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('A soma de todos os números ímpares entre 1 e 500 que são múltiplos de 3 é dada por: {}'.format(soma))