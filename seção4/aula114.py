# High Order Functions

# *args ira desempacotar ao retornar a funcao greetig
def greeting(msg, name):
    return f' The message: {msg}, and name {name}'

def execute(function, *args):
    return function(*args)

print(execute(greeting, 'Hi', 'Joao'))