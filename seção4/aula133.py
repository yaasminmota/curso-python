lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


'''def orderna(item):
    return item['nome']

# Percorre a lista. A cada dict ele chama a funcao
# A funcao retorna o valor da chave nome e no fim ele ordena esses valores
lista.sort(key=orderna)'''

def exibir (lista):
    for i in lista:
        print(i)

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['nome'])

exibir(l1)
exibir(l2)

