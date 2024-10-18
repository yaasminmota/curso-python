# Generator Functions

'''def generator(n=0):
    yield 1
    print('step one')
    yield 2
    print('step two')
    yield 3
    print('step three')
    return 'Its over'
    

gen = generator(n=0)'''

#função generation é um iteravel, 
# que ao percorrer por ela vai retornar um yield 
# (e o que estiver abaixo) de cada vez
'''for n in gen:
    print(n)'''

#generator = (n for n in range(10))

def generator(n=0,maximum=10):
    while True:
        yield n

        if n == maximum:
            return 
        
        n += 1

gen = generator()

for i in gen:
    print(i)
