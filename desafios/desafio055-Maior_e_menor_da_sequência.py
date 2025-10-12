lista_pesos = []
for i in range(0, 5):
    peso = float(input('Peso (Kg): '))
    lista_pesos.append(peso)
lista_pesos.sort()
print(lista_pesos)
print('O maior peso é {:.1f} Kg e o menor é {:.1f} Kg'.format(lista_pesos[4], lista_pesos[0]))
