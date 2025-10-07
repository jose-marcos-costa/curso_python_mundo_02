salario = float(input('Salário: R$ '))
valor_casa = float(input('Valor da casa: R$ '))
tempo_anos = int(input('Tempo (anos): '))
tempo_meses = tempo_anos * 12
prestacao = valor_casa / tempo_meses
if salario * 0.3 > prestacao:
    print('PRABÉNS! Seu empréstimo foi APROVADO!')
else:
    print('Infelizmente seu empréstimo foi NEGADO!')
print(prestacao)
print(0.3 * salario)
print(tempo_meses)