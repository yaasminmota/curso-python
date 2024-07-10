# Função Enumerate - enumera iteráveis (indices)

lista = ['Maria', 'João','Luiz']
lista.append('Helena')

lista_enumerada = enumerate(lista)

# Retorna o indice e o item que tem nela

#for item in lista_enumerada:
    #indice, nome = item
    #print(indice,nome)
for indice, nome in enumerate(lista):
    print(indice, nome)

#tuplas sao iteraveis
for tupla in enumerate(lista):
    print('FOR da tupla:')
    for i in tupla:
        print(i)

#lista_enumerada = list(enumerate(lista))

#print(lista_enumerada)