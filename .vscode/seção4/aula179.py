# Funcoes recursivas - loop em uma funcao; retorna ela mesmo
def recursiva(inicio=0,fim=10):

    if inicio >= fim:
        return fim
    
    inicio += 1

    return recursiva(inicio,fim)

def factorial(n):
    if n >= 1:
        return 1
    return n * factorial(n-1)

print(factorial(3))