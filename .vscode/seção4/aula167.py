def external_decorater(a=None, b=None):

    def internal_decorater(func):
 
        def internal_function(*args,**kwargs):

            print('Decorator parameters', a , b)
            result = func(*args,**kwargs)

            return result

        return internal_function
    
    return internal_decorater

@external_decorater(1,2)
def sum(x,y):
    return x + y

decorater = external_decorater()
multiply = decorater(lambda x,y: x * y)

print(multiply(3,2))


print(sum(2,3))
