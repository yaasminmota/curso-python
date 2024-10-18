'''
Crie funcoes que duplicam, triplicam e quadruplicam
o número recebido como parametro
'''

def multiply(value):
    def operation(multiplier):
        if multiplier == 2:
            return f'{value} x {multiplier} = {value*multiplier}'
        if multiplier == 3:
            return f'{value} x {multiplier} = {value*multiplier}'
        if multiplier == 4:
            return f'{value} x {multiplier} = {value*multiplier}'
    
    return operation

operation1 = multiply(2)
operation2 = multiply(3)
operation3 = multiply(4)

print(operation1(2))
print(operation2(3))
print(operation3(4))
