def sum(x,y):
    return f'{x} + {y} = {x+y}'

def multiplication(x,y):
    return f'{x} + {y} = {x*y}'
    

def external_function(function, x):
    def internal_function(y):
        return function(x,y)
    return internal_function

s = external_function(sum,2)
print(s(4))