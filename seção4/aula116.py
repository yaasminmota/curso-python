# CLOSURE

def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    
    return greet

s = create_greeting('Hello')

'''
Retorna onde a funcao está na memoria
print(s)'''

print(s('Maria'))