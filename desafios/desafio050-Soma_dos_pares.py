soma = 0
for i in range(0, 4):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2  == 0:
        soma += numero
if soma == 0:
    print('Nenhum número par (diferente de 0) foi digitado!')
else:
    print('A soma dos números pares digitados é {}'.format(soma))