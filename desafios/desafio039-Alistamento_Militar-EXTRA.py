from datetime import date
ano_nascimento = int(input('Por favor, digite o ano de seu nascimento (Formato AAAA): '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
idade_correta = 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
if idade < idade_correta:
    saldo = idade_correta - idade
    print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano_atual + saldo))
elif idade == idade_correta:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    saldo = idade - idade_correta
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano_atual - saldo))

