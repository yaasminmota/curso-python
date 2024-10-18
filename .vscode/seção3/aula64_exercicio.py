''' Criar uma nova string usando while que mostre -> *L*u*i*z* *O*t*á*v*i*o
'''

#nome = 'Luiz Otávio'

#i = 0 

#while i >= 0 and i <=10:
#    print(f'*{nome[i]}',end ="")
#    i += 1

nome = 'Luiz Otávio'

indice = 0
nova_str =''
while indice < len(nome):
   letra = nome[indice]
   nova_str += f'*{letra}'
   indice += 1

nova_str += '-'
print(nova_str)

