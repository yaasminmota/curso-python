# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def produto(*args):
    total = 1

    for valor in args:
        total *= valor

    return total

valores = produto(1,2,3,4)
print(valores)

# Crie uma função, fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def paridade(a):

    resultado = a % 2
    if resultado == 0:
        return print('Par')
       
    return print('Impar')

result = paridade(3)
print(result)