"""
Exemplos de Palíndromos:

APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

(Desconsiderando acentos e espaços - Input deve ser sem acentos)
"""

"""
# Versão 1 (Com FOR)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')
"""
# Versão 2 (Sem FOR)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')
