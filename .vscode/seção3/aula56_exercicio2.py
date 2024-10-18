"""
Faça um programa que avalia a hora ao usuário e, baseando-se no horário
descrito, exiba o certificado solicitado. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input('Digite as horas em números inteiros: '))

    if hora >= 0 and hora <=11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')

    else:
        print('Não conheço essa hora')

except:
    print('Você nao digitou um numero inteiro.')


