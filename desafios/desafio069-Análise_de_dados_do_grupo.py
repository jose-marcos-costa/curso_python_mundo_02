qtd_maioridade = 0
qtd_homens = 0
qtd_mulheres20 = 0
controle = 'S'
frase = 'CADASTRE UMA PESSOA'
while controle == 'S':
    print(f'-' * 30)
    print(f'{frase:^30}')
    print(f'-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Informe o sexo [M/F] ')).strip().upper()[0]
    if idade >= 18:
        qtd_maioridade += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres20 += 1
    print(f'-' * 30)
    print('Registrado com sucesso!')
    print(f'-' * 30)
    controle = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Opção Inválida! Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'{qtd_maioridade} pessoas com mais de 18 anos foram cadastradas.')
print(f'{qtd_homens} homens foram cadastrados.')
print(f'{qtd_mulheres20} mulheres com menos de 20 anos foram cadastradas.')
