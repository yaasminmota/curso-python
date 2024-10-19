# Funções decoradoras e decoradores

# essa func é p ser usada dentro da interna 
def create_function(func):
    def internal(*args):
        print("I'll check the argument")
        for arg in args:
            checking_args(arg)
        print('Its your argument is a string')
        return f'Result: {func(*args)}'

    return internal 


def checking_args(param):
    if not isinstance(param, str):
        raise TypeError('The parameter must be a string')


def reverse_string(string):
    return string[::-1]


passing_function = create_function(reverse_string)
passing_args_internal = passing_function('123') #passando arg p funcao interna
print(passing_args_internal)