from random import choice
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('###' * 10)
print('GAME:  Pedra, Papel, Tesoura')
print('###' * 10)
pessoa = str(input('Digite sua jogada: ')).strip().upper()
computador = choice(opcoes)
print('A pessoa escolheu: {}'.format(pessoa))
print('O computador escolheu: {}'.format(computador))
if pessoa == computador:
    print('EMPATOU! Jogue novamente...')
elif (pessoa == 'PEDRA' and computador == 'TESOURA') or (pessoa == 'PAPEL' and computador == 'PEDRA') or (pessoa == 'TESOURA' and computador == 'PAPEL'):
    print('Parabéns! VOCÊ GANHOU!')
elif (computador == 'PEDRA' and pessoa == 'TESOURA') or (computador == 'PAPEL' and pessoa == 'PEDRA') or (computador == 'TESOURA' and pessoa == 'PAPEL'):
    print('HAHAHA! EU GANHEI!')
