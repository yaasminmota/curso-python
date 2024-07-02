"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos Escrever "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = len(input('Digite seu nome:'))

if nome <= 4:
    print('O nome é curto')
if nome == 5 or nome ==6:
    print('Seu nome é normal')
if nome > 6:
     print('Seu nome é muito grande')