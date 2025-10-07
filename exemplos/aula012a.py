cores = {'amarelo' : '\033[1;33m',
         'azul' : '\033[1;34m',
         'verde' : '\033[1;32m',
         'roxo' : '\033[1;35m',
         'invertido' : '\033[7m',
         'limpo' : '\033[m'}
nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Gustavo':
    print('Que nome {}bonito{}!'.format(cores['verde'], cores['limpo']))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem {0}popular{1} no {0}Brasil{1}!'.format(cores['amarelo'], cores['limpo']))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome {}feminino{}!'.format(cores['roxo'], cores['limpo']))
else:
    print('Seu nome é {}normal{}!'.format(cores['azul'], cores['limpo']))
print('Tenha um bom dia, {}{}{}!'.format(cores['invertido'], nome, cores['limpo']))