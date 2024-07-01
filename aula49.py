# Introdução ao try e expect

# se digitar um numero, ele recebe como str
numero_str = input('Digite um número:')

# transformar em float para nao concatenar; veja que aqui o é possivel ser uma str e ao converter p float dara erro e para o programa
# numero_float = float(numero_str)

# se esse numero for inteiro 
#if numero_str.isdigit():
    # transformar em float para nao concatenar; veja que aqui o num é inteiro
   # numero_float = float(numero_str)
   # print(f'O dobro de {numero_str} é {numero_float*2}')
#else:
  #  print('Não é um numero inteiro')

try: 
    # converter p float
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
except:
    print('Não é um numero')