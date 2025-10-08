from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano do seu nascimento (Formato AAAA): '))
idade = ano_atual - ano_nascimento
print('O atleta tem {} anos'. format(idade))
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
"""
# Outra forma de fazer as condições:
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER') 
"""
