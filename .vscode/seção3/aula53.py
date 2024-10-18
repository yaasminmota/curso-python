# Flags - Marcar um local

condicao = False

passou_pelo_if = None

if condicao:
    passou_pelo_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# passou pelo if ou nao?; Poderia criar a var no else = false tambem, mas p aprender o conceito vamos atribuir none a var

print(passou_pelo_if)

if passou_pelo_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
