# yield from

def gen1():
    yield 'Começou gen 1'
    yield 1
    yield 2
    yield 'Acabou gen 1'

def gen2(gen=None):
    if gen is not None:
        yield from gen()
    yield 'Começou gen 2'
    yield 3
    yield 4
    yield 'Acabou gen 2'

g1 = gen1()
g2 = gen2(gen1)

for n in g2:
    print(n)