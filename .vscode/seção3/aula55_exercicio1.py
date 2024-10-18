"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero_int =int(input('Digite um número inteiro: '))
#nao tem como transformar um float(str) em int

    if numero_int % 2 == 0:
        print('O número é par.')
    else: 
        print('O número é impar.')

except: 
    print('Não é um número inteiro')

