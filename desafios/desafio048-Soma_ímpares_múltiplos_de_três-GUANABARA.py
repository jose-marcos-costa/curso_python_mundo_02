# Versão do Guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} números ímpares entre 1 e 500 que são múltiplos de 3 é dada por: {}'.format( cont, soma))
