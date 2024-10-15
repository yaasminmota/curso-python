product = {
    'name': 'blue pen',
    'prece': 2.5,
    'category': 'office',
}

dc = {
    key:value.upper() if isinstance(value,str) else value
    for key, value in product.items()
    if key == 'category'
}
#print(dc)

list = [
    ('a', 'value a'),
    ('b', 'value a'),
    ('b', 'value a'),
]

dc = {
    key:value
    for key, value in list
}
#print(dc)

set = {i *2 for i in range(3)}
print(set)
