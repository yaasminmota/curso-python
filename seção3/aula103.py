# Gerar os primeiros nove dígitos do cpf
import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

print(nove_digitos)
