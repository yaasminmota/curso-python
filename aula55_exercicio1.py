"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero_str = input('Digite um número inteiro: ')
#nao tem como transformar um float(str) em int
    numero_float = int(numero_str)

    if numero_float % 2 == 0:
        print('O número é par.')
    else: 
        print('O número é impar.')

except: 
    print('Não é um número inteiro')

