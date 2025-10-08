from datetime import date
print('''Escolha o seu gênero: 
[ 1 ] Masculino
[ 2 ] Feminino''')
genero = int(input('Sua opção: '))
if genero ==  1:
    ano_atual = date.today().year
    idade_correta = 18
    print('ALISTAMENTO OBRIGATÓRIO!')
    ano_nascimento = int(input('Ano de nascimento (Formato AAAA): '))
    idade = ano_atual - ano_nascimento
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
elif genero == 2:
    print('No Brasil, o alistamento de mulheres é VOLUNTÁRIO e NÃO OBRIGATÓRIO!')
else:
    print('Opção inválida!')

