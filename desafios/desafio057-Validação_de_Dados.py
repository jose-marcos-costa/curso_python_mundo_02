sexo = 'J'
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        print('Correto! Sexo MASCULINO digitado!')
        break
    elif sexo == 'F':
        print('Correto! Sexo FEMININO digitado!')
        break
    else:
        print('Incorreto! Digite o sexo novamente!')
print('FIM')

