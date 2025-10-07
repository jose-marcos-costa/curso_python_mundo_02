from datetime import date
ano_nascimento = int(input('Por favor, digite o ano de seu nascimento (Formato AAAA): '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Ainda vai se alistar.')
    tempo_resta = 18 - idade
    print('Ainda faltam {} ano(s) para se alistar'.format(tempo_resta))
elif idade == 18:
    print('É hora de se alistar!')
else:
    print('Já passou do tempo do ALISTAMENTO!')
    tempo_passou = idade - 18
    print('Você está {} ano(s) atrasado!'.format(tempo_passou))