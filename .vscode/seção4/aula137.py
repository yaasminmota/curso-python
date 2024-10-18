# Lista comprehension

list = [value for value in range(3)]
#print(list)
list = [value*2 for value in range(3)]
#print(list)

products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    product['name']
    for product in products
]
#print(*new_products,sep='\n')

new_products = [
    {'name':product['name'],'price':product['price']}
    for product in products
]
#print(*new_products,sep='\n')

new_products = [
    {**product, 'price':product['price'] * 2 }
    for product in products
]
#print(*new_products,sep='\n')

new_products = [
    {**product, 'price':product['price'] * 2 }
    if product['price'] > 20 else product
    for product in products
]
print(*new_products,sep='\n')

