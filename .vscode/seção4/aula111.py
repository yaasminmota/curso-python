def soma(*args):
    somar = 0
    for valores in args:
        somar += valores
    print(f'Total: {somar}')
soma(1,2,3,4,5)