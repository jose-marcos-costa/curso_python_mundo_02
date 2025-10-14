from random import randint
print(f'=-' * 14)
print(f'VAMOS JOGAR PAR OU ÍMPAR?')
print(f'=-' * 14)
venceu = True
cont = 0
while venceu:
    jogador = int(input('Diga um valor: '))
    modo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'--' * 14)
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}.', end=' ')
    print(f'Total = {total}', end=' ')
    if total % 2 == 0:
        print(f'Deu PAR')
        if modo == 'P':
            print(f'Você GANHOU!')
            cont += 1
        elif modo == 'I':
            print(f'Você PERDEU!')
            break
    else:
        print(f'Deu ÍMPAR')
        if modo == 'P':
            print(f'Você PERDEU!')
            break
        elif modo == 'I':
            print(f'Você GANHOU!')
            cont += 1
print(f'=-' * 14)
print(f'GAME OVER! Você venceu {cont} vez(es).')