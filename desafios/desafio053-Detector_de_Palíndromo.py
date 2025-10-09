"""
Exemplos de Palíndromos:

APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

(Desconsiderando acentos e espaços - Input deve ser sem acentos)
"""
cores = {
    'vermelho': '\033[1;41m',
    'verde': '\033[1;42m',
    'limpa': '\033[m'
}
frase = str(input('Digite uma frase: ')).strip().upper()
separador = ''
direto = []
invertido = []
for i in range (0, len(frase)):
    if frase[i] != ' ':
        direto.append(frase[i])
juntas = separador.join(direto)
print('A frase sem espaço tem {} caracteres'.format(len(direto)))
invertido = juntas[::-1]
print('A frase digitada sem espaços: {}'.format(juntas))
print('A frase digitada invertida: {}'. format(invertido))
if juntas == invertido:
    print('{}A frase é um PALÍNDROMO!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}A frase NÃO É UM PALÍNDROMO!{}'.format(cores['vermelho'], cores['limpa']))
