'''Cuidados com tipos de dados mutáveis
Mutaveis - aponta para o mesmo valor de memória
Imutáveis - copiado o valor
'''

lista_a = ['Maria', 123, True]
lista_b = lista_a.copy() # copia o valor da lista a 

lista_a[0] = 'João'
print(lista_a)
print(lista_b)