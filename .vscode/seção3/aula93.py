frase = ' olha só, que coisa '
lista_frase = frase.split(',')
print(lista_frase)

frase_lista = []
for i, frase in enumerate(lista_frase):
    frase_lista.append(lista_frase[i].strip())
    
print(lista_frase)
print(frase_lista)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)