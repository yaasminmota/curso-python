# Funcoes lambdas

def sum(x,y):
    return x + y

def execute(function, *args):
    return function(*args)

print(execute(sum,2,2))
print(execute(lambda x,y: x+y, 2, 2))
