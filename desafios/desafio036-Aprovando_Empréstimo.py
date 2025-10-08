valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
tempo = int(input('Tempo (anos): '))
prestacao = valor_casa / (tempo * 12)
print('Para pegar um empréstimo de R$ {:.2f} em {} anos,'.format(valor_casa, tempo), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if salario * 0.3 > prestacao:
    print('PARABÉNS! Seu empréstimo foi APROVADO!')
else:
    print('Infelizmente seu empréstimo foi NEGADO!')
#print(prestacao)
#print(0.3 * salario)
#print(tempo_meses)