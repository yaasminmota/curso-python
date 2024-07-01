# Fatiamento de string e função len

# 012345678
# Olá mundo
#-987654321  

variavel = 'Olá mundo'
print(f'A frase é: {variavel[::1]}')
print(f'A frase invertida é: {variavel[::-1]}')
print(f'Aas duas primeiras letras: {variavel[0:2]}')
print(variavel[-2:]) 
print(variavel[-1:-2:-1]) # de tras p frente
