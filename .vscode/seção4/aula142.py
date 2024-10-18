list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Luiz'},
]

for item in list:
    if isinstance(item, set):
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print(item.upper())
        
    elif isinstance(item, (int, float)):
        print(item, item* 2)

    else:
        print('Other type: ', item )