list = []

for x in range(3):
    for y in range(3):
        list.append((x,y))
print(list)

# Fazendo o mesmo com list comprehension

list = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(list)

list =[
    [value for value in range(3)]
    for i in range(3)
]
print(list)

list = [
    [(f'{i} = {letter}') for letter in 'Luiz']
    for i in range(3)
]
print(list)