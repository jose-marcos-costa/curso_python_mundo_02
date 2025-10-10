# Solução do Guanabara - Gasta menos processamento
for n in range(2, 51, 2):
    print(n, end=' ')
print('\nACABOU')
# Não é o número de linhas que influencia no processamento e sim as repetições. Fez em bateladas (de 2 em 2)

"""
##### Minha solução #####
for i in range(1, 51):
    if i % 2 == 0:
        print('O número {:2} é PAR!'.format(i))
"""