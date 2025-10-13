from random import randint
palpites = 0
computador = randint(0, 10)
print('Sou seu computador... Acabei de pesnsar em um número entre 0 e 10.')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
