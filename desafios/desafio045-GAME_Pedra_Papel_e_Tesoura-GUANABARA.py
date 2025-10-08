from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if 0 <= jogador <= 2:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:     # Computador jogou PEDRA
        if jogador == 0:    # Jogador também jogou PEDRA
            print('EMPATE')
        elif jogador == 1:  # Jogador jogou PAPEL
            print('JOGADOR VENCEU')
        elif jogador == 2:  # Jogador jogou TESOURA
            print('COMPUTADOR VENCEU')
    elif computador == 1:   # Computador jogou PAPEL
        if jogador == 0:    # Jogador jogou PEDRA
            print('COMPUTADOR VENCEU')
        elif jogador == 1:  # Jogador também jogou PAPEL
            print('EMPATE')
        elif jogador == 2:  # Jogador jogou TESOURA
            print('JOGADOR VENCEU')
    elif computador == 2:   # Computador jogou TESOURA
        if jogador == 0:    # Jogador jogou PEDRA
            print('JOGADOR VENCEU')
        elif jogador == 1:  # Jogador jogou PAPEL
            print('COMPUTADOR VENCEU')
        elif jogador == 2:  # Jogador também jogou TESOURA
            print('EMPATE')
else:
    print('Opção Inválida!')
