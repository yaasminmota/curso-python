from itertools import groupby
#antes de agrupar por dados, eles também tem que estar ordenados
list = [1,1,3,1,2,2,3]
ordered_list = sorted(list)
print(ordered_list)

group = groupby(list)

#groupby retorna pares de chave, valor e a chave é o agrupamento
# a chave é outro iteravel(os valores do agrupamento)

for key, value in group:
    print(key)
    print(list(value))

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

ordered_students = sorted(students, key=lambda dict:dict['nota'])
group_students  = groupby(ordered_students, key=lambda a:a['nota'])

for grouping, values in group_students:
    print(grouping, list(values))

