# Exiba os índices da lista

lista = ['Maria', 123, True]
#possui 
indices = range(len(lista))

print(indices)

for i in indices:
   print(f'indice {i}: {lista[i]}, {type(lista[i])} ')