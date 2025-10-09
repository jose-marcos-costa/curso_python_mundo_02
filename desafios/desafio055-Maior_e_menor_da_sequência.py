lista_pesos = []
for i in range(0, 5):
    peso = int(input('Peso (Kg): '))
    lista_pesos.append(peso)
lista_pesos.sort()
print(lista_pesos)
print('O maior peso é {} Kg e o menor é {} Kg'.format(lista_pesos[4], lista_pesos[0]))


