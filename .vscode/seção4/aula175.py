from itertools import groupby
#antes de agrupar por dados, eles também tem que estar ordenados
lista = [1,1,3,1,2,2,3]
lista_ordenada = sorted(lista)
print(lista_ordenada)

grupos = groupby(lista)

#groupby retorna pares de chave, valor e a chave é o agrupamento
# a chave é outro iteravel(os valores do agrupamento)

for chave, valor in grupos:
    print(chave)
    print(list(valor))

alunos = [
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

alunos_ordenados = sorted(alunos, key=lambda dict:dict['nota'])
grupos_alunos  = groupby(alunos_ordenados, key=lambda a:a['nota'])

for agrupamento, valores in grupos_alunos:
    print(agrupamento, list(valores))

