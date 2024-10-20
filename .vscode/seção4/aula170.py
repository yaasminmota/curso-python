# min(), zip()

from itertools import zip_longest

def zipper(list1, list2):
    shortest_list = min(len(list1), len(list2))
    return [(list1[i],list2[i]) for i in range(shortest_list)]

print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ']))

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1,l2)))

print(list(zip_longest(l1,l2,fillvalue='Sem valor')))