# Empacotamento e desempacotamento de dicionarios

pessoa = {
    'nome':'Maria',
    'sobrenome':'Souza'
}

dados_pessoa = {
    'idade': 15,
    'altura': 1.6
}
# atribuir chave e valor em uma var
a, b = pessoa.items() #retorna duas tuplas
#print(a, b)
(a1,a2),(b1,b2) = pessoa.items()
#print(a1, a2, b1, b2)
pessoa_completo = {**pessoa, **dados_pessoa, 'idade':18}
#print(pessoa_completo)

# Args e kwargs

def mostro_argumentos(*args,**kwargs):

    print('Argumentos sem nome:', args)
    for chave, valor in kwargs.items():
        print(f'Argumentos nomeados: {chave}, {valor}')
    

#mostro_argumentos(1,2, nome='Joana')
mostro_argumentos(pessoa_completo)