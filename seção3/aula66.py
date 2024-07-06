#Calculadora usando while

# loop infinito que so sera interrompido caso queira sair

while True:
    #apenas para declarar fora dos blocos
    num_1 = None
    num_2 = None
    operador = None
    #usar flag valores p checar se deu erro no try
    valores = None

    try:
        num_1 = float(input('Digite o primeiro número: '))
        num_2 = float(input('Digite o segundo número: '))
        operador = input('Digite o operador (+-/*): ')
        valores = True
    except :
        #se der erro nos try (num_1,num_2 e operador) a flag valores continua none
        if valores is None:
            print('Alguns dos valores estão inválidos')
            continue

    #tratamento de erro para o operador
    operador_permitido = '+-/*'
    if len(operador) > 1:
        print('É apenas um operador.')
        continue    
    if operador not in operador_permitido:
        print('Operador inválido.')
        continue 
     
    if operador == '+':
        print(f'{num_1} + {num_2} = {num_1 + num_2}')
    elif operador == '-':
        print(f'{num_1} - {num_2} = {num_1 - num_2}')
    elif operador == '/':
        print(f'{num_1} / {num_2} = {num_1 / num_2}')
    elif operador == '*':
        print(f'{num_1} * {num_2} = {num_1 * num_2}')
    else:
        print('Erro inesperado')

    sair = input("Você deseja sair? [S]im ou [N]ão?:").lower().startswith('s')

    if sair is True:
        break
    