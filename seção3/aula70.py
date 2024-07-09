# Iterando strings com while
# Qual letra apareceu mais vezes na frase?

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
aparece_mais = 0
letra_mais_vezes = ''

while i < len(frase):

    letra = frase[i]
    qte = frase.count(letra)
    i += 1

    if letra == ' ':
        continue

    print(f'{letra} = {qte}')

    if aparece_mais < qte:
        aparece_mais = qte
        letra_mais_vezes = letra

print(f' A letra {letra_mais_vezes} aparece {aparece_mais} vezes.')