"""
# Primeira versão (sem medição de tempo de execução)

soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('A soma de todos os números ímpares entre 1 e 500 que são múltiplos de 3 é dada por: {}'.format(soma))
"""

"""
# Primeira versão (com medição de tempo de execução)

from time import perf_counter
tempo_inicial = perf_counter()
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print('A soma de todos os números ímpares entre 1 e 500 que são múltiplos de 3 é dada por: {}'.format(soma))
tempo_final = perf_counter()
tempo_decorrido = tempo_final - tempo_inicial
print('{}'.format(tempo_decorrido))
"""

# Segunda versão (com medição de tempo de execução)

from time import perf_counter
tempo_inicial = perf_counter()
soma = 0
for i in range(3, 501, 2):
    if i % 3 == 0:
        soma += i
        #print(i, end=' ')
print('A soma de todos os números ímpares entre 1 e 500 que são múltiplos de 3 é dada por: {}'.format(soma))
tempo_final = perf_counter()
tempo_decorrido = tempo_final - tempo_inicial
print('{}'.format(tempo_decorrido))
