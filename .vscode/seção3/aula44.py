# Interpolação de strings

nome = 'Maria'
preco = 198.32
  
print('o nome é %s:' % nome)
print('O nome é %s e o preço é %.2f' % (nome, preco))
print('-' * 30)
print('O hexadecimal de %d é %x' % (1500,1500))
print('O hexadecimal é %x' % 1500)

print(f'{nome: >10}')
print(f'{nome: ^10}') # centraliza
