from datetime import date
cont_maior = 0
ano_atual = date.today().year
for i in range (0, 7):
    ano_nascimento = int(input('Ano de Nascimento (AAAA): '))
    idade = ano_atual - ano_nascimento
    print('Sua idade é {}'.format(idade))
    if idade >= 18:
        cont_maior += 1
print('\n{} pessoas já atingiram a maior idade'.format(cont_maior), end='')
print('\n{} pessoas ainda não atingiram a maioridade!'.format(7 - cont_maior))