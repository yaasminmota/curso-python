from functools import partial

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#funcao p desempacotar a lista e printar cada indice
def print_iter(iterator):
    print(*iterator, sep='\n')

def increase_percentage(value, percentage):
    return round(value*percentage,2)

increase_ten_percent = partial(increase_percentage, percentage = 1.1)
'''
new_products = [
    #faz copia de p, se alterar essa lista nao afeta a original
    {**p,  'preco': increase_ten_percent(p['preco'])}
    for p in products
    ]'''

def change_price_product(product):
    return {**product, 'preco':increase_ten_percent(product['preco'])}

# precorre cada item de products e passa como parametro p funcao
# o que for retornado vai ser cada indice de um obj iteravel
# um obj iteravel so pode ser usado uma vez, assim transforma ele em uma lista
new_products = list(map(change_price_product, products))

#print_iter(new_products)

new_products = filter(lambda p:p['preco'] > 10, products)
print_iter(list(new_products))



