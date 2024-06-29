# Método format em strings

nome = 'Maria'
idade = 19

#pessoa = 'Idade = {1}, Nome = {0}'.format(nome, idade)
#print(pessoa)

# Aqui já chama os arg de acordo com o indice do metodo format
dados1 = 'Idade = {1}, Nome = {0}'

pessoa1 = dados1.format(nome, idade)

print(pessoa1)

# criando parametros para os argumentos e chamando pelos parametros
dados2 = "Idade = {idade1}, Nome = {nome1}"
pessoa2 = dados2.format(idade1=idade, nome1=nome)
print(pessoa2)
