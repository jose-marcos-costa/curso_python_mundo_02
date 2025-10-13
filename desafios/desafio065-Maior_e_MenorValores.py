cont = 0
soma = 0
media = 0
maior = 0
menor = 0
opcao = 'S'
while opcao != 'N':
    cont += 1
    numero = int(input('\nDigite um número inteiro: '))
    soma += numero
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    opcao = str(input('\nDeseja continuar [S/N]: ')).strip().upper()
media = soma / cont
print('Média = {:.2f}'.format(media), end='\n')
print('Maior = {}'.format(maior), end='\n')
print('Menor = {}'.format(menor))
