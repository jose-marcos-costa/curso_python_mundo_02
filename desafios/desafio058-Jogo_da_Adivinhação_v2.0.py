from time import sleep
from random import randint
cont = 0
numero_jogador = 11
numero_computador = randint(0, 10)
print('PENSANDO',end='')
sleep(0.5)
print('*', end='')
sleep(0.5)
print('*', end='')
sleep(0.5)
print('*')
sleep(0.5)
print('PENSEI!\n')
while numero_jogador != numero_computador:
    cont += 1
    numero_jogador = int(input('Digite um número (0 a 10): '))
    if numero_jogador == numero_computador:
        print('Você ACERTOU! O número escolhido foi {} e você precisou de {} palpite(s) para acertar'.format(numero_computador, cont))
    else:
        print('Tente novamente!')