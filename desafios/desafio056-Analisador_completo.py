media = 0
cont = 0
lista_nomes = []
lista_idades = []
lista_generos = []
n_pessoas = 4
maior = 0
for i in range(0, n_pessoas):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i+1))).strip().capitalize()
    lista_nomes.append(nome)
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    lista_idades.append(idade)
    print('[ M ] Masculino\n[ F ] Feminino')
    genero = str(input('Opção escolhida: ')).strip().upper()
    lista_generos.append(genero)
    if genero == 'F' and idade < 20:
        cont += 1
    if genero == 'M' and idade > maior:
        maior = idade
        aux = i
media = sum(lista_idades) / n_pessoas
print('A média de todas as idades é {:.2f}'.format(media))
print('{} é o homem mais velho'.format(lista_nomes[aux]))
print('Há {} mulher(es) com menos de 20 anos'.format(cont))