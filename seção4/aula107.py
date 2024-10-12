"""
Valores padrão para parâmetros em funções

Usa-se o valor padrão (NoneType) caso não é enviado um argumento

"""

def soma(x, y, z=None):

    # Este caso é apenas se usar um if 
    if z:
        print(f'A soma de {x=} e {y=} e {z=} é:', x + y + z)
    #print(f'A soma de {x=} e {y=} é: {x + y}')
    else:
        print(f'A soma de {x=} e {y=}  é:', x + y )
# Se passar uma string vazia ou 0 é false 
soma(2,2)