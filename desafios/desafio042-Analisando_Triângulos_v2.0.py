a = int(input('Digite a medida da primeira semireta (a): '))
b = int(input('Digite a medida da segunda semireta (b): '))
c = int(input('Digite a medida da terceira semireta (c): '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('SIM! As 3 semiretas formam um triângulo!')
    if a == c and c == b:
        print("Triângulo Equilátero!")
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles')
    elif a != b and b != c:
        print('Triângulo Escaleno')
else:
    print('NÃO! As 3 semiretas não formam um triângulo')

