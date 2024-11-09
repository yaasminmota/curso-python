from functools import reduce

# reduce(funcao c/ 2 parametros, iteravel, primeiro valor a ser somado)
# o primeiro valor a ser somado vai ser o primeiro arg da funcao,
# o primeiro valor do iteravel vai ser o segundo arg

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

new_products = [
    p['preco']
    for p in products
]

sum_price = reduce(lambda x,y:  x+y, new_products, 0)
# o primeiro valor a ser retornado vai ser arg de x e o arg de y vai ser o proximo item
print(round(sum_price,2))
print(roun(sum(new_products)))