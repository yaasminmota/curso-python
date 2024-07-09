# For/in - Estrutura de repetição para coisas finitas

'''
senha = '123456'
senha_atual = ''

repeticoes = 0

while senha_atual != senha:
    senha_atual = input(f'Digite a senha ({repeticoes}x) :')
    repeticoes += 1
'''

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto)