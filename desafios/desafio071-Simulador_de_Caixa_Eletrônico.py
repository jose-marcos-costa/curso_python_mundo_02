valores_disponiveis = (50, 20, 10, 1)
numero_notas = [0, 0, 0, 0]
valor_desejado = int(input('Digite o valor desejado: R$ '))
cont = 0
while valor_desejado > 0:
    if valor_desejado // valores_disponiveis[cont] > 0:
       numero_notas[cont] = valor_desejado // valores_disponiveis[cont]
       print(f'Total de {numero_notas[cont]} notas de R$ {valores_disponiveis[cont]}')
       valor_desejado = valor_desejado - numero_notas[cont] * valores_disponiveis[cont]
       cont += 1
    else:
        cont +=1
        continue
# print(numero_notas)
"""
if valor_desejado // valores_disponiveis[0] > 0:
    numero_notas_50 = valor_desejado // valores_disponiveis[0]
    print(f'{numero_notas_50} notas de R$50', end=' ')
    valor_desejado = valor_desejado - numero_notas_50 * valores_disponiveis[0]
if valor_desejado // valores_disponiveis[1] > 0:
    numero_notas_20 = valor_desejado // valores_disponiveis[1]
    print(f'{numero_notas_20} notas de R$20', end=' ')
    valor_desejado = valor_desejado - numero_notas_20 * valores_disponiveis[1]
if valor_desejado // valores_disponiveis[2] > 0:
    numero_notas_10 = valor_desejado // valores_disponiveis[2]
    print(f'{numero_notas_10} notas de R$10', end=' ')
    valor_desejado = valor_desejado - numero_notas_10 * valores_disponiveis[2]
"""





