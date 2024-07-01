# Operadores in e not in

#nome = 'Isabele'

#print('be' in nome)
#print('za' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Que parte você quer encontrar?: ')

if encontrar in nome:
    print(f'"{encontrar}" está em {nome}')

else:
    print(f'"{encontrar}" não está em {nome}')
